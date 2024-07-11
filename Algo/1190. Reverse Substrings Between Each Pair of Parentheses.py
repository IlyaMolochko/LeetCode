class Solution:
    def reverseParentheses(self, s: str) -> str:
        answ = []
        result = []
        for c in s:
            if c == '(':
                answ.append([])
            elif c == ')':
                suf = answ.pop()[::-1]
                if answ:
                    answ[-1].extend(suf)
                else:
                    result.extend(suf)
            elif answ:
                answ[-1].append(c)
            else:
                result.append(c)
        return ''.join(result)
