class Solution(object):
    def removeKdigits(self, num, k):
        st = []
        for ch in num:
            while k>0 and st and st[-1]>ch:
                st.pop()
                k -= 1
            st.append(ch)
        while k>0:
            st.pop()
            k -= 1
        a = ''.join(st).lstrip("0")
        if a == "":
            return "0"
        else:
            return a