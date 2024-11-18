class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # use topological sort, Kahn's algorithm
        # directed acyclic graph (DAG)
        # do postorder traversal DFS
        # 11/18/24) Sun night) 123-147am) tk)
        adjacency_list = defaultdict(set)
        # adj = { c:set() for w in words for c in w}
        for w in words:
            for c in w:
                if c not in adjacency_list:
                    adjacency_list[c] = set()

        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            minlen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minlen] == w2[:minlen]:
                return ""
            for j in range(minlen):
                if w1[j] != w2[j]:
                    adjacency_list[w1[j]].add(w2[j])
                    break
        
        # now do postorder DFS
        visited = {} # False means visited, True means its on the current path (not visited)
        result = []
        def dfs(char1):
            if char1 in visited:
                return visited[char1]
            visited[char1] = True

            for nei in adjacency_list[char1]:
                if dfs(nei):
                    return True
            visited[char1] = False
            result.append(char1)
            return False
        
        for c in adjacency_list:
            if dfs(c):
                return ""
        result.reverse()
        return "".join(result)
        

        