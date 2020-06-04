# Problem Link : https://leetcode.com/problems/minimum-path-sum/

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[0 for i in grid[0]] for j in grid]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                dp[i][j] += grid[i][j]
                if i > 0 and j > 0:
                    dp[i][j] += min(dp[i - 1][j], dp[i][j - 1])
                elif j > 0:
                    dp[i][j] += dp[i][j - 1]
                elif i > 0:
                    dp[i][j] += dp[i - 1][j]
        
        if len(grid):
            return dp[-1][-1]
        else:
            return 0
                