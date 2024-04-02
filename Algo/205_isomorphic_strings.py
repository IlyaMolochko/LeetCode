class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dct1 = defaultdict(int)
        dct2 = defaultdict(int)
        for i in range(len(s)):
            if s[i] not in dct1:
                dct1[s[i]] = t[i]
                if t[i] in dct2:
                    return False
                dct2[t[i]] = s[i]
            elif dct1[s[i]] != t[i]:
                return False
        return True
