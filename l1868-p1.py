class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        # O(m+n)
        i,j = 0,0
        ans = []
        # 11/25/24) Sun night) tk) 118-129am)
        while i < len(encoded1) and j < len(encoded2):
            v1, f1 = encoded1[i]
            v2, f2 = encoded2[j]

            product = v1*v2
            cur_min = min(f1, f2)

            if ans and ans[-1][0] == product:
                ans[-1][1] += cur_min
            else:
                ans.append([product, cur_min])
            
            encoded1[i][1] -= cur_min
            encoded2[j][1] -= cur_min
            if encoded1[i][1] == 0:
                i+= 1
            if encoded2[j][1] == 0:
                j+= 1
        return ans