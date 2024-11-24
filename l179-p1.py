class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # 11/24/24) Sun) 122-128pm) tk) makerlab)
        arr = list(map(str, nums))
        arr.sort(key=lambda x:x*10, reverse = True) #custom sorting using lambda functions
        if arr[0] == "0":
            return "0"
        result = "".join(arr)
        return result
