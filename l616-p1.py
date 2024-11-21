class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        # similar to leetcode 56 - merge intervals, and same as leetcode 758 - bold words in string
        intervals = []
        # 11/21/24) Thurs) 224 to 243pm) tk)
        for w in words: # gather the intervals
            start = s.find(w)
            while start != -1:
                intervals.append([start, start+len(w)])
                start = s.find(w, start+1) # find the next instance of the same word
        
        if not intervals:
            return s
        # now merge intervals
        intervals.sort()
        merged = [intervals[0]]

        for curr in intervals[1:]:
            prev = merged[-1]
            if curr[0] <= prev[1]:
                prev[1] = max(prev[1], curr[1])
            else:
                merged.append(curr)

        #now assemble the result
        res = []
        prev_end = 0

        for start, end in merged:
            res.append(s[prev_end:start])
            res.append(f"<b>{s[start:end]}</b>")
            prev_end = end
        res.append(s[prev_end:])
        return "".join(res)