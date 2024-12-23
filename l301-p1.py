class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
    # Remove Invalid Parentheses - LeetCode
    # Remove Invalid Parentheses - Optimized BFS
    # Time Complexity: O(n * 2^n), Space Complexity: O(n * 2^n)

    # 12/23/24) Sun night) gtk) 1222 to 1229am) 12J

        def isValid(string):
            balance = 0
            for char in string:
                if char == '(':
                    balance += 1
                elif char == ')':
                    balance -= 1
                    if balance < 0:  # Early termination for invalid state
                        return False
            return balance == 0

        # BFS setup
        queue = [s]
        visited = set(queue)
        res = []
        found = False

        while queue:
            next_level = []
            for string in queue:
                if isValid(string):
                    res.append(string)
                    found = True  # If valid string found, do not process deeper levels
                if not found:  # Only generate substrings if no valid string has been found
                    for i in range(len(string)):
                        if string[i] not in '()':  # Skip non-parenthesis characters
                            continue
                        candidate = string[:i] + string[i + 1:]
                        if candidate not in visited:
                            visited.add(candidate)
                            next_level.append(candidate)
            if found:
                break  # Exit early if any valid string is found
            queue = next_level

        return res

