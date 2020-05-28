# Problem Link : https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # anchors = []
        anchor = -1
        for explorer in range(len(nums)):
            if nums[explorer] == 0 and anchor == -1:
                anchor = explorer
            if nums[explorer] != 0 and anchor != -1:
                temp = nums[explorer]
                nums[explorer] = nums[anchor]
                nums[anchor] = temp
                for i in range(anchor + 1, explorer + 1):
                    if nums[i] == 0:
                        anchor = i
                        break
        return nums
                