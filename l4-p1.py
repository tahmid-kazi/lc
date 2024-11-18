class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 11/17/24) 836 to 933pm) Sun) tk)
        # use binary search (O log(m+n))
        A, B = nums1, nums2
        total_len = len(nums1) + len(nums2)
        half = total_len//2

        if len(A) > len(B):
            A, B = B, A     # we need the smaller array

        left, right = 0, len(A) - 1 # two-pointer binary search only on the smaller array
        
        while True:
            i = (left + right)//2   # to traverse the smaller array A
            j = half - i - 2        # to traverse the bigger array B
            
            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i+1] if (i+1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j+1] if (j+1) < len(B) else float("infinity")

            # if the partitioning is already correct
            if Aleft <= Bright and Bleft <= Aright:
                if total_len % 2 == 1:
                    #if total length is odd number, just return the min
                    return min(Aright, Bright)
                else:
                    #if total length is even number, calculate median
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            # if partition not correct:
            elif (Aleft > Bright):
                right = i-1
            else:
                left = i+1