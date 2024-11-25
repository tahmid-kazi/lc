class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search
        # 11/25/24) Mon) tk) 517-527pm) bbus)
        # nested functions are faster
        def canEatAll(piles, h, k):
            hours = 0
            for pile in piles:
                hours += (pile + k -1)//k # equivalent to math.ceil()
            return hours <= h
            
        left, right =  1, max(piles)
        while left < right:
            mid = (right+left)//2
            if canEatAll(piles, h, mid):
                right = mid
            else:
                left = mid+1
        return left
    