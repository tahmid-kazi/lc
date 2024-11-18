class Solution:
    def isNumber(self, s: str) -> bool:
        # uses FSM, regex or string parsing (all of them O(n) time and O(1) space complexity)
        # similar to leetcode 8 - atoi
        # my approach = manual parsing
        # 11/18/24) 731-810am) Mon) tk)
        s = s.strip()
        if not s:
            return False
        
        def isInteger(part):
            if not part:
                return False
            if part[0] in "+-":
                part = part[1:]
            return part.isdigit()
        
        def isDecimal(part):
            if not part:
                return False
            if part[0] in "+-":
                part = part[1:]
            if part.count('.') != 1:
                return False
            left, _, right = part.partition('.')
            # At least one side of the decimal must have digits
            if left and not left.isdigit():
                return False
            if right and not right.isdigit():
                return False
            # Both sides cannot be empty
            return (left.isdigit() or right.isdigit())

        # Check if the string contains 'e' or 'E' for scientific notation
        if 'e' in s or 'E' in s:
            # Split the string into base and exponent parts
            # Use the first occurrence of 'e' or 'E'
            e_index = s.find('e') if 'e' in s else s.find('E')
            base = s[:e_index]
            exponent = s[e_index+1:]
            # Both base and exponent must be valid
            return (isInteger(base) or isDecimal(base)) and isInteger(exponent)
        else:
            # If there's no exponent, the string must be a valid integer or decimal
            return isInteger(s) or isDecimal(s)