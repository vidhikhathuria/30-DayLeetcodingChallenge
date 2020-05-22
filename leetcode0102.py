# Problem Link: https://leetcode.com/problems/happy-number/

class Solution:
    def isHappy(self, n: int) -> bool:
        
        def calc(n):
            s = 0
            while n != 0:
                var = n % 10
                s += var ** 2
                n -= var
                n = int(n / 10)
            return s
        
        
        slow, fast = n, calc(n)
        if slow == 1 or fast == 1:
            return True
        while slow != fast:
            slow = calc(slow)
            fast = calc(calc(fast))
            if fast == 1:
                return True
        return False
        