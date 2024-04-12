class Solution:
    def trap(self, height: List[int]) -> int:
        answ = 0
        st = []
        for i in range(len(height)):
            while st and height[i] > height[st[-1]]:
                top = st[-1]
                st.pop()
                if st:
                    w = i - st[-1] - 1
                    h = min(height[i], height[st[-1]]) - height[top]
                    answ += h * w
            st.append(i)
        return answ
