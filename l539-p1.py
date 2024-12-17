class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # 12/16/24) Mon) tk) 1053/1100-1102pm)
        # convert time string to minutes since midnight
        def to_minutes(time: str) -> int:
            hours, minutes = map(int, time.split(':'))
            return hours*60 + minutes

        # first convert the time string to minutes and sort them
        minutes = sorted(to_minutes(time) for time in timePoints)

        # then calculate the min difference by comparing adjacent times
        min_diff = float('inf')
        for i in range(1, len(minutes)):
            min_diff = min(min_diff, minutes[i] - minutes[i-1])
        
        # now check for (day wraps around at 1440mins)
        min_diff = min(min_diff, 1440-(minutes[-1]-minutes[0]))

        return min_diff