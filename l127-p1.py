class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # use BFS, use a queue + set()
        # 11/23/24) 758-806pm) Sat) tk)
        wordset = set(wordList)
        if endWord not in wordset:
            return 0
        
        wordqueue = deque([beginWord])
        changes = 1

        while wordqueue:
            size = len(wordqueue)
            changes += 1
            for _ in range(size):
                currword = wordqueue.popleft()
                for i in range(len(currword)):
                    for j in range(26): #try all lowercase chars
                        temp = currword[:i] + chr(ord('a')+j) + currword[i+1:]

                        if temp == endWord:
                            return changes
                        
                        if temp in wordset:
                            wordqueue.append(temp)
                            wordset.remove(temp)
        return 0

        