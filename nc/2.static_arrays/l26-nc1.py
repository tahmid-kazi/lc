class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        ptr1 = 1
        # 12/31/24) 1034-1050pm) Tue night) tk) vabch-nctk)
        while ptr1 < len(nums):
            if nums[ptr1] == nums[ptr1-1]:
                del nums[ptr1] #this keeps dynamically updating the array so your ptr1 value increment needs to adjust accordingly
            else:
                k += 1
                ptr1 += 1
        return k
