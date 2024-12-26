class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # first calculate all the distances (for loop)
        # fill up the distance array
        # then sort
        # then take the first k elements
        # 12/26/24) 1202-1215pm) Thurs) tk) 12J) 5th problem of the day)
        # 1216pm) this is actually kinda fun
        dists = []
        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]
            dist1 = (x**2+y**2)**0.5
            dists.append((dist1, [x,y]))
        dists.sort()
        results = []
        for j in range(k):
            results.append(dists[j][1])
        return results