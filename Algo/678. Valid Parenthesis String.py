class Solution:
    def checkValidString(self, s: str) -> bool:
        o = 0
        c = 0
        for i in s:
            if i == '(':
                o += 1
                c += 1
            elif i == ')':
                o = max(0, o - 1)
                c -= 1
            elif i == '*':
                o = max(0, o - 1)
                c += 1
            if c < 0:
                return False
        
        return o == 0
