class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        # 11/12/24) Tue) 1144-1149pm) tk) (11th problem of the day done!)
        pref = strs[0]
        for i in strs[1:]:
            while not i.startswith(pref):
                pref = pref[:-1] #continually trim the pref
                if pref == "":
                    return ""
        return pref
