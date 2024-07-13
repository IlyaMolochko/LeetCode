class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        ids = list(range(n))
        answ = []
        st = []
        ids.sort(key=lambda x: positions[x])
        for idx in ids:
            if directions[idx] == 'R':
                st.append(idx)
            else:
                while st and healths[idx] > 0:
                    top = st.pop()
                    if healths[top] > healths[idx]:
                        healths[top] -= 1
                        healths[idx] = 0
                        st.append(top)
                    elif healths[top] < healths[idx]:
                        healths[idx] -= 1
                        healths[top] = 0
                    else:
                        healths[idx] = 0
                        healths[top] = 0
        for i in range(n):
            if healths[i] > 0:
                answ.append(healths[i])
        
        return answ
