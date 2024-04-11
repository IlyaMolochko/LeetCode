class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st = []
        for i in range(len(num)):
            while st and num[i] < st[-1] and k > 0:
                st.pop()
                k -= 1
            if num[i] != '0' or st:
                st.append(num[i])
        
        while st and k > 0:
            st.pop()
            k -= 1
        if not st:
            return '0'
        return ''.join(st)
