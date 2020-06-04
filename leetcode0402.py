# Problem Link : https://leetcode.com/problems/bitwise-and-of-numbers-range/

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        c = 0
        while m != n:
            m = m >> 1
            n = n >> 1
            c += 1
            # print(m, n)
        return m << c
        