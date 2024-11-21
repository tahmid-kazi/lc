class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 11/20/24) 1111-1117pm) Wed) tk)
        i = 0 #acts as point a pointer and a counter
        for k in range(len(nums)):
            if nums[k] != val:
                nums[i] = nums[k]
                i += 1
        return i
        