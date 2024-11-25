class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        rs = 0 # 11/25/24) tk) Mon) 1029-1032am)
        intervals.sort(key=lambda x: x[1])
        end = float('-inf')
        for interval in intervals:
            if interval[0] < end:
                rs += 1
            else:
                end = interval[1]
        return rs