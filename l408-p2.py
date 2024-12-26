class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        # race pointers
        # 12/25/24) 1051-1100pm) Wed) tk)
        ptr1, ptr2 = 0, 0
        while ptr1 < len(word) and ptr2 < len(abbr):
            if abbr[ptr2].isalpha():
                if word[ptr1] != abbr[ptr2]:
                    return False
                #move both by 1
                ptr1 += 1
                ptr2 += 1
            else:
                # you forgot the edge case of 0
                if abbr[ptr2] == "0": #when it starts, this is carefully sequentially placed
                    return False
                num = 0
                while ptr2 < len(abbr) and abbr[ptr2].isdigit():
                    num = num*10+int(abbr[ptr2])
                    ptr2 += 1
                ptr1 += num
        return ptr1 == len(word) and ptr2 == len(abbr)