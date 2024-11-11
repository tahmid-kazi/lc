class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # 11/10/24) Sun) 654-656pm) tk)
        # return str(int(num1)+int(num2))
        
        # two-pointer approach (11/10/24)(Sun)(1127-1129pm) tk)
        i, j, carry = len(num1)-1, len(num2)-1, 0
        ans = ""

        while i >= 0 or j >= 0 or carry == 1:
            if i >= 0:
                carry += ord(num1[i]) - ord('0') #ord() is the unicode representation
                i -= 1
            if j >= 0:
                carry += ord(num2[j]) - ord('0')
                j -= 1
            #else
            ans += chr((carry%10)+ord('0'))
            carry //= 10
        return ans[::-1]