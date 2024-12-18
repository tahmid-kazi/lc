class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # you cant use / * % operators (856 to 905pm)
        # bruh2 = int(dividend / divisor)
        # if bruh2 > 2**31-1 or bruh2 < -2**31:
        #     return 0
        # return bruh2
        # 12/17/24) Tue) 856-927pm) tk) 
        # edge case
        if dividend == -2**31 and divisor == -1:
            return 2**31-1

        # deal with sign
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            sign = -1
        else:
            sign = 1
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0
        #now use bit manipulation to do the actual division
        while dividend >= divisor:
            current_divisor = divisor
            current_multiple = 1

            while dividend >= (current_divisor << 1): #check the next step before running the next step
                current_divisor <<= 1
                current_multiple <<= 1
            
            dividend -= current_divisor
            quotient += current_multiple
        quotient *= sign
        return max(min(quotient, 2**31-1), -2**31)
