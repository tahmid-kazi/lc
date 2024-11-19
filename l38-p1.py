class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        # 11/19/24) Tue) 455-507pm) tk) 
        def nextOne(next):
            result = []
            i = 0
            while i < len(next):
                count = 1
                # RLE (Run length encoding)
                while i+1 < len(next) and next[i] == next[i+1]:
                    i += 1
                    count += 1
                result.append(str(count)+next[i])
                i += 1
            return "".join(result)
        next1 = "1"
        for _ in range (2, n+1):
            next1 = nextOne(next1)
        return next1
