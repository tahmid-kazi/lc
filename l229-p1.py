class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # did Leetcode 169 - majority element on 11/13/24
        # 11/21/24) thurs) 514-527pm) tk)        
        hashmap = defaultdict(int)
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1

        res = []
        for key, val in hashmap.items():
            if val > len(nums)//3:
                res.append(key)
        return res

        # follow up: if you want to solve it in O(n) time and O(1) space = Boyer-Moore Majority vote algorithm
