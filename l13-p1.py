class Solution:
    def romanToInt(self, s: str) -> int:
        mappings = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        value = 0
        # 12/18/24) Wed) 826-834pm) tk)
        
        # O(n) runtime (most optimal), space = O(1)

        for i in range(len(s)-1): # loop until 2nd to last char
            # e.g. roman numeral = III or LVIII (the largest number is usually first (as in s[0]))
            if mappings[s[i]] < mappings[s[i+1]]:
                value -= mappings[s[i]]
            else:
                value += mappings[s[i]]
        value += mappings[s[-1]] # last roman numeral
        return value