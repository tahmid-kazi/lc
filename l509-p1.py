class Solution:
    def fib(self, n: int) -> int:
        # 12/10/24) Tue night) 1153pm-1201am) tk)
        cache = {0:0, 1:1}
        def fib2(n):
            if n in cache:
                return cache[n]
            else:
                cache[n] = fib2(n-1)+fib2(n-2)
                return cache[n]
        return fib2(n)