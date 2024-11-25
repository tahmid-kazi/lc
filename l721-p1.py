class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # this should be a dictionary mapping of the first name to all their emails
        # bruh nevermind this is a graph/union-find problem wtf??
        # dict1 = defaultdict(list)

        # for a in accounts:
        #     if a[0] in dict1:
        #         for x in range(1, len(a)):
        #             dict1[a[0]].append(x)
        #     else:
        #         dict1[a[0]] = a
        # return list(dict1.values())

        # try1 = 829-841pm) 11/20/24) Wed)

        # done (try2) = 11/25/24) Sun night) 129-146am) tk)
        parent = {}
        
        def find(x): # find() function with path compression
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y): # union function (hence union-find)
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:
                parent[root_y] = root_x
        # 1st initialize Union-Find for all emails
        email_to_name = {}
        for account in accounts:
            name = account[0]
            first_email = account[1]
            for email in account[1:]:
                if email not in parent:
                    parent[email] = email
                email_to_name[email] = name
                union(first_email, email)

        #2nd group emails by root parent
        groups = defaultdict(list)
        for email in parent:
            root = find(email)
            groups[root].append(email)

        # 3rd format the result
        result = []
        for root, emails in groups.items():
            result.append([email_to_name[root]] + sorted(emails))
        return result
