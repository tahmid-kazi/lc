class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # 11/6/24) Tue night) 115 to 130am) tk)
        dict1 = defaultdict(list)
        for j in strs:
            sorted_word = ''.join(sorted(j))
            if sorted_word not in dict1:
                dict1[sorted_word] = [j]
            else:
                dict1[sorted_word].append(j)
        
        return list(dict1.values())