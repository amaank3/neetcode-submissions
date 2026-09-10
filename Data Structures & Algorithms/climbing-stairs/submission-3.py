class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {1:1, 2:2}
        if n <=2:
            return n
        if n in cache:
            return cache[n]

        cache[n]= self.climbStairs(n-1) + self.climbStairs(n-2)

        return cache[n]

        
        