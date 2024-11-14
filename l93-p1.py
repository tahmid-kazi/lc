class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # 11/13/24) Wed) 748/832 to 854pm) tk)
        result = []
        def backtracking(start_idx, path):

            if len(path) == 4:
                if start_idx == len(s):
                    result.append(".".join(path))
                return

            for i in range(1,4):
                if start_idx + i > len(s):
                    break

                part = s[start_idx: start_idx+i]
                if (part[0] == '0' and len(part) > 1) or int(part) > 255:
                    continue
            
                backtracking(start_idx + i, path + [part])

        backtracking(0, [])
        return result