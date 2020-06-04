# Problem Link : https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = 0
        for i in range(len(nums)):
            if reach < i:
                return False
            s = i + nums[i]
            if s > reach:
                reach = s
        # if reach == len(nums) - 1:
        #     return True
        return True