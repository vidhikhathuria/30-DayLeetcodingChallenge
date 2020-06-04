# Problem Link : https://leetcode.com/problems/longest-common-subsequence/

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for i in range(len(text1) + 1)] for j in range(len(text2) + 1)]
        # for i in dp:
        #     print(i)
        for i in range(len(text2)):
            for j in range(len(text1)):
                # print()
                # for k in dp:
                #     print(k)
                if text1[j] == text2[i]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
        return dp[-1][-1]