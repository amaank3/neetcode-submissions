class Solution:
    def climbStairs(self, n: int) -> int:
        # Bottom up dp
        if n <=2:
            return n

        dp = [1,2]
        i = 3
        while i <=n:   
            tmp = dp[1]
            dp[1] = dp[0]+dp[1]
            dp[0] = tmp
            i+=1

        return dp[1]





        # Top down memoization
        # cache = {1:1, 2:2}
        # if n <=2:
        #     return n
        # if n in cache:
        #     return cache[n]

        # cache[n]= self.climbStairs(n-1) + self.climbStairs(n-2)

        # return cache[n]

        
        