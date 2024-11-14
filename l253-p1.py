class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # 11/14/24) Thurs) (1221-1239pm) tk)
        if not intervals:
            return 0
        intervals.sort()        
        conf_rooms = [intervals[0]]

        for i in range(1, len(intervals)):
            curr = intervals[i]
            replace = False
            for k in range(len(conf_rooms)):
                room = conf_rooms[k]
                if curr[0] >= room[1]: # if the start time of the current node is greater than the end time of the existing booking, replace it with the latest time that the conference room will be in use
                    conf_rooms[k] = curr
                    replace = True
                    break
            if not replace: #if there is no replacement (as in 2 meetings happening at the same time)
                conf_rooms.append(curr) #you need 2 conference rooms if you have meeting conflict
        return len(conf_rooms)