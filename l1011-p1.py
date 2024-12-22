class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # 1125 to 1155am) logs
        # binary search, (O(n*log(sum(weights)-max(weights))) time, O(1) space) 
        
        # done (12/22/24) (Sun) (344 to 352pm) tk) 12J
        def can_ship_with_capacity(capacity): # O(n)
            current_weight = 0
            required_days = 1
            for w in weights:
                if current_weight + w > capacity:
                    required_days += 1
                    current_weight = 0
                current_weight += w
            return required_days <= days
        
        #now run binary search (O(logn))
        left, right = max(weights), sum(weights)
        while left < right:
            mid = (left+right)//2
            if can_ship_with_capacity(mid):
                right = mid
            else:
                left = mid+1
        return left
