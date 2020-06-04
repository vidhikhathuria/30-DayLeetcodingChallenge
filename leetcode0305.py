# Problem Link : https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not len(nums):
            return -1
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + int((right - left) / 2)
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        # print(left, nums[left])
        start = left
        left = 0
        right = len(nums) - 1
        if target >= nums[start] and target <= nums[right]:
            left = start
        else:
            right = start
        while left <= right:
            mid = left + int((right - left) / 2)
            # print(mid, nums[mid])
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return -1