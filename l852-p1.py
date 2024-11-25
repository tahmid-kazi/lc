class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # binary search
        # did this before I think, for google
        # 11/25/24) Mon) tk) 512-517pm) bbus)
        left, right = 0, len(arr)
        while left < right:
            mid = (left+right)//2
            if arr[mid-1]<arr[mid] and arr[mid+1]<arr[mid]:
                return mid
            elif arr[mid-1] > arr[mid] and arr[mid+1] < arr[mid]:
                right = mid
            else:
                left = mid

