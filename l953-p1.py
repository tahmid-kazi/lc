class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
    # Verifying an Alien Dictionary - LeetCode
    # Time Complexity: O(n * l), Space Complexity: O(1)
    
    # 12/23/24) gtk) sun night) 1229 to 1231am) 12J
        order_index = {c: i for i, c in enumerate(order)}
        # youre allowed to use a double for loop here
        for i in range(len(words) - 1):
            for j in range(len(words[i])):
                if j >= len(words[i + 1]):
                    return False
                if words[i][j] != words[i + 1][j]:
                    if order_index[words[i][j]] > order_index[words[i + 1][j]]:
                        return False
                    break
        return True
            