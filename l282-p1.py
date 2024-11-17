class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        # 11/17/24) Sun) (1233-1253pm) + (239-249pm) tk)
        # this is similar to 224) basic calculator & 227) basic calculator II 
        #should be recursive backtracking
        def backtrack(index, path, value, last):
            if index == len(num):
                if value == target:
                    result.append(path)
                return 
            
            for i in range(index, len(num)):
                if i > index and num[index] == "0":
                    break
                
                curr = int(num[index:i+1])
                if index == 0:
                    backtrack(i+1, path+str(curr), curr, curr)
                else:
                    # 3 operations
                    backtrack(i+1, path + "+" + str(curr), value + curr, curr) # addition
                    backtrack(i+1, path + "-" + str(curr), value - curr, -curr) # subtraction
                    backtrack(i+1, path + "*" + str(curr), value - last + last * curr, last*curr) # multiplication

        result = []
        backtrack(0, "", 0, 0)
        return result