class Solution:
    def compress(self, chars: List[str]) -> int:
        answ = 0
        ch = None
        cnt = -1
        for i in range(len(chars)):
            if ch is None:
                cnt = 1
                ch = chars[i]
            elif ch == chars[i]:
                cnt += 1
            else:
                chars[answ] = ch
                answ += 1
                if cnt > 1:
                    s = str(cnt)
                    chars[answ:answ + len(s)] = list(s)
                    answ += len(s)
                cnt = 1
                ch = chars[i]
        if cnt > 1:
            chars[answ] = ch
            answ += 1
            s = str(cnt)
            chars[answ:answ + len(s)] = list(s)
            answ += len(s)
        elif cnt == 1:
            chars[answ] = ch
            answ += 1
        return answ
