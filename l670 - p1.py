class Solution:
    def maximumSwap(self, num: int) -> int:
        # 11/12/24) Tue) (659/723 - 739pm) done tk)
        num1 = list(str(num))
        # first create a hashmap keeping track of the last occurence of each digit
        hashmap = {}
        for j in range(len(num1)):
            hashmap[int(num1[j])] = j
        
        for i in range(len(num1)):
            for d in range(9, int(num1[i]), -1):
                if d in hashmap and hashmap[d] > i:
                    num1[i], num1[hashmap[d]] = num1[hashmap[d]], num1[i]
                    return int("".join(num1))

        return num