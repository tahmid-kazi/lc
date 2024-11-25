class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # DP with cache (bottom up) (probably wont be asked)
        # runtime = O(n+D), space = O(D) or in some cases O(1) (most optimal) if you keep a rolling array for last 30days cost
        # 11/25/24) Sun night) 1248-1259am) tk) 
        last_day = days[-1]
        travel_days = set(days)
        cache = [0] * (last_day+1)
        for i in range(1, last_day+1):
            if i not in travel_days:
                cache[i] = cache[i-1]
            else:
                cache[i] = min(
                    cache[i-1] + costs[0], # 1-day pass
                    cache[max(0,i-7)] + costs[1], # 7-day pass
                    cache[max(0, i-30)] + costs[2] # 30-day pass
                )
        return cache[last_day]