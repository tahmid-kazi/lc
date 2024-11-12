class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        # 11/11/24) Mon) 844 to 912pm) tk)
        # bruh google asked me this during my interview!! (the interval question)
        intervals = []

        # use two pointer approach
        i = j = 0

        while i < len(firstList) and j < len(secondList):
            # calculate the potential start and end points first
            start = max(firstList[i][0], secondList[j][0])
            end = min(firstList[i][1], secondList[j][1])

            if start <= end:
                intervals.append([start, end])
            
            first_list_endpoint = firstList[i][1]
            second_list_endpoint = secondList[j][1] 
            if first_list_endpoint < second_list_endpoint: #so that you can see if the second item in the first list might have some overlap with the first item in the second list
                i += 1
            else:
                j += 1

        return intervals