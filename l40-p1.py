class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # recursive backtracking with cache
        # 947-1012pm, 1036-1042pm) 11/20/24) Wed) tk)
        candidates.sort()
        res = []
        temp = []

        def findcombo(idx, target):
            if target == 0: #we found the valid combo 
                res.append(temp[:])
                return
            #else:
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue #skip duplicates
                if candidates[i] > target:
                    break #skip larger than target items
                temp.append(candidates[i])
                findcombo(i+1, target-candidates[i]) # O(2^n)
                temp.pop()
        findcombo(0, target)
        return res