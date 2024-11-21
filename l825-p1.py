class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        # 11/20/24) Wed) 847/906-916pm) tk) 
        ages.sort()
        send_request = 0
        # helper function/ run binary search
        # def binary_search(arr, target):
        #     left, right = 0, len(arr)
        #     while left < right:
        #         mid = (left+right)//2
        #         if target < arr[mid]:
        #             right = mid
        #         else:
        #             left = mid+1
        #     return left

        # the actual code
        for i in range(len(ages)):
            if ages[i] < 14:
                continue
            lower_bound = 0.5*ages[i]+7

            #left = binary_search(ages, lower_bound)
            #right = binary_search(ages, ages[i]) # revisit
            left = bisect.bisect_right(ages, lower_bound)  # Find the first valid age > lower_bound
            right = bisect.bisect_right(ages, ages[i])    # Find the first age > ages[i]
            

            send_request += max(0, right-left-1)

        return send_request