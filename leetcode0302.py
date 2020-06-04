# Problem Link : https://leetcode.com/problems/valid-parenthesis-string/

class Solution:
    def checkValidString(self, s: str) -> bool:
        op = []
        star = []
        for i in range(len(s)):
            if s[i] == '(':
                op.append(i)
            elif s[i] == '*':
                star.append(i)
            else:
                if len(op):
                    op.pop()
                elif len(star):
                    star.pop()
                else:
                    return False
            print(op, star)
        while len(op):
            opening = op.pop()
            if len(star):
                st = star[-1]
                if opening < st:
                    star.pop()
                else:
                    return False
            else:
                return False
        if len(op):
            return False
        return True