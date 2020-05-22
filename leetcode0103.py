# Problem Link: https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        start = 0
        s = -99999999999
        m = s
        for i in range(len(nums)):
            if sum(nums[start: i + 1]) <= nums[i]:
                start = i
                s = nums[i]
            else:
                s += nums[i]
            if s > m:
                m = s
        return m
         