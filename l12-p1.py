class Solution:
    def intToRoman(self, num: int) -> str:
        # divide by 1000, it turns into M
        # then divide by 500 it turns into D
        # divide remainder by 100, it turns into C, and so on
        
        # 11/19/24) Tue) 1041-1052pm) tk)
        if num == 0:
            return ''
        
        value_symbols = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), 
            (9, 'IX'), (5, 'V'), (4, 'IV'), (1,'I')
        ]

        res = []
        for val, sym in value_symbols:
            count = num // val # the number of M's and so on
            res.append(sym * count) # res = [MMM, ...] and so on
            num -= count * val # num = num - 3000
        
        return "".join(res)