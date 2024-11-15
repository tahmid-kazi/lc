class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # 11/15/24) Fri) 235 to 305pm) tk) 
        result = ""
        dic = {}
        for key in s:
            if key in dic:
                dic[key] += 1
            else:
                dic[key] = 1
        
        for i in order:
            if i in s:
                for key in dic:
                    if i == key:
                        result += i * dic[key]
        
        for i in s:
            if i not in result:
                for key in dic:
                    if i == key:
                        result += i * dic[key]

        return result
