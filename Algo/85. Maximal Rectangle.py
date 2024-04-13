class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        answ = 0
        hist = [0] * len(matrix[0])

        for row in matrix:
            for i in range(len(row)):
                hist[i] = hist[i] + 1 if row[i] == '1' else 0
            res = 0
            st = []
            for i in range(len(hist) + 1):
                while st and (i == len(hist) or hist[st[-1]] > hist[i]):
                    h = hist[st.pop()]
                    w = i if not st else i - st[-1] - 1
                    res = max(res, h * w)
                st.append(i)
            answ = max(answ, res)
        return answ
