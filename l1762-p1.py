class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        # 11/11/24) 942/954-1012pm) tk) Mon)
        # monotonic stack solution
        stack1 = []
        for i in range(len(heights)):
            # if the previous height is less than the current height, that means that the current height can block the ocean view of the previous building.
            # heights[stack[-1]] is equal to heights[i-1] (for example)
            while stack1 and heights[stack1[-1]] <= heights[i]:
                stack1.pop()
            stack1.append(i)
        return stack1