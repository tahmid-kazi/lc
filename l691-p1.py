# class Solution:
#     def minStickers(self, stickers: List[str], target: str) -> int:
#         # this is dynamic programming, probably wont be asked
#         # 123-143am) 11/24/23) Sat night) tk)
#         m = len(target)
#         n = 1 << m
#         cache = [float('inf')] * n
#         cache[0] = 0

#         sticker_count = [Counter(sticker) for sticker in stickers]

#         for state in range(n):
#             if cache[state] == float('inf'):
#                 continue
#             for sticker in sticker_count:
#                 new_state = state
#                 current_sticker = sticker.copy()
#                 for i in range(m):
#                     char = target[i]
#                     if (state >> i) & 1==0 and current_sticker[char] > 0:
#                         current_sticker[char] -= 1
#                         new_state |= (1<<i)
#                 cache[new_state] = min(cache[new_state], cache[state]+1)
#         return cache[n-1] if cache[n-1] != float('inf') else -1


# more optimized
# 11/24/24) Sat night) 235-255am) tk)
class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        target_count = Counter(target)
        sticker_counts = [Counter(sticker) & target_count for sticker in stickers]

        for i in range(len(sticker_counts)-1, -1, -1):
            if any (sticker_counts[i] == (sticker_counts[i] & sticker_counts[j])
                for j in range(len(sticker_counts)) if i != j):
                sticker_counts.pop(i)
        stickers = ["".join(sticker.elements()) for sticker in sticker_counts]

        @cache
        def min_stickers(current_sticker, bitmask):
            if bitmask == (1 << len(target)) - 1:
                return 0
            if current_sticker == len(stickers):
                return float("inf")
            result = min_stickers(current_sticker+1, bitmask)
            new_bitmask = bitmask
            for char in stickers[current_sticker]:
                for i in range(len(target)):
                    if not (new_bitmask & (1<<i)) and target[i] == char:
                        new_bitmask |= (1<<i)
                        break
            
            if new_bitmask != bitmask:
                result = min(result, 1+min_stickers(current_sticker, new_bitmask))
            return result
        result = min_stickers(0, 0)
        return result if result != float("inf") else -1