# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        if not s:
            return None
        # 11/9/24) 1147am/1209-1232pm) Sat) tk)
        # use stack + iterative approach, not dfs+preorder
        i = 0
        stack1 = []
        while i < len(s): # iterate through the entire string
            # 1: when you encounter a ")"
            if s[i] == ")":
                stack1.pop()
                i+=1
            
            # 2: when you encounter a number
            elif (s[i].isdigit() or s[i]=='-'):
                #now construct the number
                start = i
                while i < len(s) and (s[i]=='-' or s[i].isdigit()):
                    i+=1
                constructed_num = int(s[start:i])
                node = TreeNode(constructed_num)

                #now there the whole stack thing
                if stack1:
                    parent = stack1[-1]
                    if not parent.left:
                        parent.left = node
                    else:
                        parent.right = node
                stack1.append(node)

            # 3: when you encounter a "("
            else:
                i+=1
        # end of while loop
        if stack1:
            return stack1[0]
        else:
            return None