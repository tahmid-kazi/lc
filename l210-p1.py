class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # use topological sort, Kahn's algorithm, BFS (queue)
        # 12/18/24) tk) Wed) 1015 to 1035pm) 
        # runtime: O(V+E), space O(V+E)
        
        graph = defaultdict(list) # adjacency list
        prereq_count = [0] * numCourses # track the number of prerequisites for each course
        # [course, prereq] is the format in which the data is represented
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            prereq_count[course] += 1 # e.g. prereq count for course 2 is 1, for course2 is 5 and so on

        queue1 = deque()
        order = []
        for i in range(numCourses): # fill the queue to run the BFS
            if prereq_count[i] == 0:
                queue1.append(i)

        while queue1:
            course = queue1.popleft()
            order.append(course)

            for neighbor in graph[course]: 
                prereq_count[neighbor] -= 1
                if prereq_count[neighbor] == 0:
                    queue1.append(neighbor) # the BFS section 
        return order if len(order) == numCourses else []
