class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # 10/9/24, 1128pm to 1145pm, Wed night
        intervals.sort()
        result_intervals = []

        for j in intervals:

            if not result_intervals: #why do we need this?
                result_intervals.append(j)
            if j[0] <= result_intervals[-1][1]: # check to see if the end interval of the last item is less than the start interval of the current item.
                left = result_intervals[-1][0] #the new left
                right = max(j[1], result_intervals[-1][1]) #the new right
                new_item = [left, right]
                
                #now remove the last item
                result_intervals.pop()
                #and enter in the newly constructed item
                result_intervals.append(new_item)
            else:
                result_intervals.append(j)

        return result_intervals 
