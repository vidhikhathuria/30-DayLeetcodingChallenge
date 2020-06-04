# Problem Link : https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        hashmap = defaultdict(int)
        hashmap[0] = 1
        s = 0
        c = 0 
        for i in nums:
            # print(hashmap)
            s += i
            if s - k in hashmap:
                c += hashmap[s - k]
            hashmap[s] += 1
        return c