class Solution:
    def numberToWords(self, num: int) -> str:

    # Integer to English Words - LeetCode
    # Time Complexity: O(n), Space Complexity: O(1)

    # 12/23/24) sun night) gtk) 212 to 215am) 

        if num == 0:
            return "Zero"

        # Define mappings for number groups
        below_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
                    "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", 
                    "Seventeen", "Eighteen", "Nineteen"]

        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

        thousands = ["", "Thousand", "Million", "Billion"]

        # Helper function to convert numbers below 1000
        def helper(num):
            if num == 0:
                return ""
            elif num < 20:
                return below_20[num] + " "
            elif num < 100:
                return tens[num // 10] + " " + helper(num % 10)
            else:
                return below_20[num // 100] + " Hundred " + helper(num % 100)

        # Main logic
        res = ""
        for i, unit in enumerate(thousands):
            if num % 1000 != 0:
                res = helper(num % 1000) + unit + " " + res
            num //= 1000

        return res.strip()
