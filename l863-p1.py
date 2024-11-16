# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # unweighted graph traversal problem
        # 11/15/24) 706 to 722pm) Fri) tk)
        if not root:
            return []
        # first build the adjacency list (graph)
        graph = defaultdict(list)
        def build_graph(node, parent):
            if node:
                if parent:
                    graph[node.val].append(parent.val)
                    graph[parent.val].append(node.val)
                build_graph(node.left, node)
                build_graph(node.right, node)
        build_graph(root, None)

        # then run BFS
        queue1 = deque([(target.val, 0)]) #tuple = (value, distance)
        visited = set() #for graphs you need visited set for BFS
        visited.add(target.val)
        results = []

        while queue1:
            node, distance = queue1.popleft()
            if distance == k:
                results.append(node)
            if distance < k:
                for nei in graph[node]:
                    if nei not in visited:
                        visited.add(nei)
                        queue1.append((nei, distance+1))
        return results