class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:

        # 11/4/24) Mon) 140pm to 159pm) tk)
        # use two pointer approach (for two strings)
        left, right = 0, 0

        while left < len(word) and right < len(abbr):
            if abbr[right].isalpha():
                #error check first
                if word[left] != abbr[right]:
                    return False

                #if its an alphabet, add +1 to both
                left += 1
                right += 1

            else:
                #edge case
                if abbr[right] == "0":
                    return False
                
                #now the most important part:
                # make the abbreviation

                num = 0
                while right < len(abbr) and abbr[right].isdigit():
                    num = 10*num+int(abbr[right])
                    right += 1
                left += num
            
        # now check if you made it to the end
        return left == len(word) and right == len(abbr)