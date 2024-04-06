class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        o = 0
        c = 0
        st = []
        for i in range(len(s)):
            if s[i] == '(':
                st.append(s[i])
                o += 1
            elif s[i] == ')' and o >= c + 1:
                st.append(s[i])
                c += 1
            elif not s[i] == ')' and not s[i] == '(':
                st.append(s[i])
        i = len(st) - 1
        while i >= 0 and o > c:
            if st[i] == '(':
                st[i] = ''
                o -= 1
            i -= 1
        return ''.join(st)
