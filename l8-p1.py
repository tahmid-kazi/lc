class Solution:
    def myAtoi(self, s: str) -> int:
        # 11/14/24) (1253-1258pm) + (117-129pm) thurs) tk)
        # this is used in Leetcode 9 - palindrome number!!
        s = s.strip()
        if not s:
            return 0
        # deal with the optional sign in front
        s1, start = [], 0
        sign = 1
        if s[0] == "-":
            sign = -1
            start = 1
        elif s[0] == "+":
            start = 1

        # deal with the digits
        for i in range(start, len(s)):
            if s[i].isdigit():
                s1.append(s[i])
            else:
                break #it has to be a contiguous number string
        
        if not s1:
            return 0
        
        str1 = "".join(s1)
        int1 = sign * int(str1)

        # number clamping
        int_min, int_max = -2**31, 2**31-1
        if int1 < int_min:
            return int_min
        if int1 > int_max:
            return int_max    
        return int1
        