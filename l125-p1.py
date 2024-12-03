class Solution:
    def isPalindrome(self, s: str) -> bool:

        #(10/8/24)(927am)(Tue) (in capital One cafe!!)
        #(10/8/24)(930pm-934pm)(Tue)
        
        newstr = ""

        for i in range(len(s)):
            if s[i].isalnum():
                newstr += s[i].lower()
        
        return newstr == newstr[::-1]