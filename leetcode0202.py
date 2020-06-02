# Problem Link : https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def make(s):
            ans = ''
            for i in s:
                if len(ans) and i == '#':
                    ans = ans[0:len(ans) - 1]
                elif not len(ans) and i == '#':
                    continue
                else:
                    ans += i
            return ans
        
        return make(s) == make(t)