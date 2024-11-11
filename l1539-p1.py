class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # 11/10/24) Sun) 1108 to 1118pm) tk)
        # use two pointer approach
        i, count, current = 0, 0, 1
        while count < k:

            if i < len(arr) and arr[i] == current:
                i+=1
            else:
                count +=1
                if count == k:
                    return current
            current+=1

        