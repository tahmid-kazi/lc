class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        # graph problem
        # time: O(n), space: O(n)
        
        # 12/19/24) Thurs) 1134-1150pm) tk)
        # first build the graph
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # then run recursive dfs
        def dfs(node, parent):
            total_time = 0
            for child in graph[node]:
                if child != parent:
                    child_time = dfs(child, node)
                    if child_time > 0 or hasApple[child]:
                        total_time += child_time+2
            return total_time
        return dfs(0,-1)