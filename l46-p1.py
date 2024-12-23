class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        # from google (aug 2024)(blind 75 classic)
        # 12/22/24) 1150-1156pm) Sun) gtk) 12J) reused
        if len(nums) == 1:
            return [nums[:]]

        else:
            for i in range(len(nums)):
                n = nums.pop(0)

                var = self.permute(nums)

                for j in var:
                    j.append(n)
                results.extend(var)
                nums.append(n)
            return results
