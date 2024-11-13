class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # 11/12/24) Tue) 1124-1139pm) tk)
        strf = ""
        len1, len2 = len(word1), len(word2)
        
        for j in range(min(len1,len2)):
            strf += word1[j] #always add word1 first
            strf += word2[j]
        
        if len1 < len2:
            strf += word2[len1:]
        elif len2 < len1:
            strf += word1[len2:]
        return strf
    
        
        # if len1 < len2: # word2 is longer
        #     for j in range(len1):
        #         strf += word1[j] #always add word1 first
        #         strf += word2[j]
        #     strf+= word2[len1:]
        # if len2 < len1: # word1 is longer
        #     for j in range(len2):
        #         strf += word1[j] #always add word1 first
        #         strf += word2[j]
        #     strf+= word1[len2:]
        # else:
        #     for j in range(len1):
        #         strf += word1[j] #always add word1 first
        #         strf += word2[j]
        # return strf