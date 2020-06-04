# Problem Link : https://leetcode.com/problems/maximal-square/

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0:
            return 0
        dp = [[0 for i in range(len(matrix[0]) + 1)] for j in range(len(matrix) + 1)]
        largest = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    dp[i + 1][j + 1] = 1 + min(dp[i][j], dp[i + 1][j], dp[i][j + 1])
                    largest = max(int(dp[i + 1][j + 1]), largest)
            #     print(matrix[i][j], end=' ')
            # print()
        return largest ** 2