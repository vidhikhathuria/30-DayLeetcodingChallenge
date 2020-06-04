# Problem Link : https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, arr: List[int]) -> List[int]:
        temp = 1
        ans = [1 for i in range(len(arr))]
        for i in range(len(arr)):
            ans[i] *= temp
            temp *= arr[i]
        temp = 1
        for i in range(len(arr) - 1, -1, -1):
            ans[i] *= temp
            temp *= arr[i]
        return ans
        