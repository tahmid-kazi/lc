class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        # 11/16/24) Sat) 1015 to 1040pm) tk)
        diagonals = defaultdict(list)
        for r in range(len(nums)):
            for c in range(len(nums[r])):
                diagonals[r+c].append(nums[r][c]) #first group the items based on what diagonal they fall in

        result = [] # then flatten it into one list  
        for key in sorted(diagonals.keys()):
            diagonal = diagonals[key]
            for item in reversed(diagonal): #reversed() is because of the how the diagonals are meant to be ordered (see diagram)
                result.append(item) 
        
        return result


        