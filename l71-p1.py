class Solution:
    def simplifyPath(self, path: str) -> str:
        # bruh I got asked this in the Meta phone screen!!
        # 11/10/24) Sun) 557 to 611pm) tk)
        # use a stack-based approach
        arr = path.split('/')
        if arr[-1] == "/": #take care of that corner case
            arr.pop()
        stack1 = []
        for k in range(len(arr)):
            if arr[k] == "." or arr[k]=="": #handle NOP
                continue
            elif arr[k] == "..":
                if stack1:
                    stack1.pop()
            else:        
                stack1.append(arr[k])

        path2 = "/".join(stack1) #this joins every element in the array/stack delimited by "/"
        return "/"+path2
        