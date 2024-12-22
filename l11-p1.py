class Solution:
    def maxArea(self, height: List[int]) -> int:
        # +b 3rd or 4th (357 to 409pm)
        # 12/22/24) tk) Sun) (409 to 412pm) done, 12J
        # two pointer, blind75 classic
        # O(n) time, O(1) space
        max_area = 0
        left, right = 0, len(height)-1

        while left < right:
            max_area = max(max_area, (right-left) * min(height[left], height[right]))

            if height[left] < height[right]:
                left += 1
            else:
                right -=1
        return max_area