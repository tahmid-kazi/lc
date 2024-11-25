class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # try1 = 829-841pm) 11/20/24) Wed)
        # done (try2) = 11/25/24) Sun night) 129-152am) tk)
        parent = {}
        
        def find(x): # find() function with path compression
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y): # union function (hence union-find)
            parent[find(y)] = find(x)
    
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
