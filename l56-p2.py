class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # 12/25/24) Wed) 1209pm) gtk) 12J
        # most optimal solution: n*log(n) runtime, O(n) space
        # similar to leetcode 986 - interval list intersection
        
        if not intervals:
            return []
        
        # Sort intervals based on the starting value
        intervals.sort(key=lambda x: x[0])
        merged = []

        for interval in intervals:
            # If merged is empty or the current interval does not overlap with the last, append it
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # Otherwise, there is overlap, so merge the current and last intervals
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
