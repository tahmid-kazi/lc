class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # use stack [], O(n) time, O(n) space
        # 12/20/24) Thurs night) tk) 333 to 349am) 

        stack = [-1]
        max_area = 0

        for i in range(len(heights)):
            while stack[-1] != -1 and heights[i] <= heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1
                max_area = max(max_area, height*width)
            stack.append(i)
        
        while stack[-1] != -1:
            height = heights[stack.pop()]
            width = len(heights) - stack[-1] - 1
            max_area = max(max_area, height * width)
        return max_area