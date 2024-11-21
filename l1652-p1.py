class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        # skipped (930-940pm) 11/20/24
        # sliding window
        # 247-256pm, 322-327pm) 11/21/24)thurs) tk)
        n = len(code)
        ans = [0] * n
        
        if k == 0: 
            return ans
        # use sliding window approach for both, just reverse it if k < 0
        if k > 0:
            start, end = (1, k)
        else:
            start, end = (n+k, n-1)

        wsum = sum(code[i%n] for i in range(start, end+1))

        for i in range(n):
            ans[i] = wsum
            # now move the sliding window
            wsum -= code[start % n] # remove outgoing element
            wsum += code[(end+1) % n] # add incoming element
            start += 1
            end += 1
        return ans