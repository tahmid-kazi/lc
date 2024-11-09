class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        # 11/9/24) 1117 to 1147am) Sat) tk)
        # finally first one of the day done!!
        #calculate distance
        #then sort the distance array and return k points
        dists = []

        for i in range(len(points)): # O(n)
            #calculate distance:
            x = points[i][0]
            y = points[i][1]
            distance = (x**2+y**2)**0.5
            dists.append((distance, [x,y]))
        
        dists.sort() #O(nlogn)
        res = []
        #now all you have to do is take k items and store them into res
        for i in range(k):
            res.append(dists[i][1])
        return res