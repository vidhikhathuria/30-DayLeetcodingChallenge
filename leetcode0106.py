# Problem Link : https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        
        ans = defaultdict(list)
        for st in strs:
            ans[tuple(sorted(st))].append(st)
        return list(ans.values())