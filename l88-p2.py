class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # stared at it + solved it on own, beats 100% (607/614-630pm) (12/25/24) Wed) tk) 12J 
        i, j, k = m-1, n-1, m+n-1
        while i >= 0 and j >= 0:
            # this means that BOTH of them need to be above/equal zero, otherwise while loop will exit
            if nums1[i] < nums2[j]:
                nums1[k] = nums2[j]
                j -= 1
            else:
                nums1[k] = nums1[i]
                i -= 1
            k -= 1
        while j >= 0: #this covers the edge cases if nums1 and nums2 have different number of elements
            nums1[k] = nums2[j]
            j -= 1
            k -= 1