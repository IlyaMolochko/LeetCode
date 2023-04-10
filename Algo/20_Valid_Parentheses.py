class Solution:
    def isValid(self, s: str) -> bool:
        st = list()
        dct = {")": "(", "]":"[", "}":"{"}
        for c in s:
            if len(st) == 0 or c not in dct:
                st.append(c)
            elif st[-1] == dct[c]:
                st.pop()
            else:
                return False
        return len(st) == 0
