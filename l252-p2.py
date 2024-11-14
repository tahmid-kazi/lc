class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # 11/13/24) Wed) 1054 to 1058pm) tk)
        intervals.sort()
        for i in range(len(intervals)-1):
            if intervals[i][1] > intervals[i+1][0]:
                return False
        return True

        # set1 = set()
        # # 11/13/24) wed) 1046 to 1054pm) tk)
        # for i in intervals:
        #     for j in range(i[0], i[1]):
        #         if j not in set1:
        #             set1.add(j) # basically add every hour that you are booked for meetings
        #         else:
        #             return False # if theres even one meeting time conflict, game over
        # return True