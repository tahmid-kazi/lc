class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        # the_num = int("".join(str(d) for d in digits))
        # result = the_num+1 
        # return list(str(result))

        # 11/12/24) Tue) 1106 to 1112pm) tk)
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        return [1] + digits