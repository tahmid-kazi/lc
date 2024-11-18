class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        # no intuition, only memorization
        # 11/18/24) 401-417pm) Mon) tk)
        pattern_matcher = defaultdict(list)
        for str1 in strings:
            if len(str1) == 1:
                pattern_matcher[(-1,)].append(str1)
            else:
                char_diffs = []
                i = 1 #start from index 1 so that you can check the diff with idx 0
                while i < len(str1):
                    char_diffs.append((ord(str1[i])- ord(str1[i-1])) % 26)
                    i += 1
                pattern_matcher[tuple(char_diffs)].append(str1)
        return list(pattern_matcher.values())