class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # iterate from end
        # time: O(max(m, n)), space: O(max(m, n))
        # 12/20/24) tk) Thurs night) 257/305-312am)
        result = []
        i,j,carry = len(a)-1, len(b)-1, 0

        while i >= 0 or j >= 0 or carry:
            x = int(a[i]) if i>=0 else 0
            y = int(b[j]) if j>=0 else 0
            total = x+y+carry
            result.append(str(total%2))
            carry = total // 2
            i -= 1
            j -= 1
        return ''.join(result[::-1])