class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # monotonic stack
        # 11/26/24) Tue) 932-948am) tk) ffx)
        n = len(arr)
        prev_smaller = [-1] * n
        next_smaller = [n] * n
        stack = []
        # calculate prev_smaller and next_smaller in one loop
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                next_smaller[stack.pop()] = i
            if stack:
                prev_smaller[i] = stack[-1]
            stack.append(i)

        #update results using contributions
        mod = 10**9 + 7
        result = 0
        for i in range(n):
            left_contrib = i - prev_smaller[i]
            right_contrib = next_smaller[i]-i
            result += arr[i] * left_contrib * right_contrib
            result %= mod
        return result