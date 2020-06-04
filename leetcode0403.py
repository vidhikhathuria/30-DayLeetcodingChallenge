# Problem Link : https://leetcode.com/problems/lru-cache/

class LRUCache:

    def __init__(self, capacity: int):
        self.q = [-1] * capacity
        self.d = {}

    def get(self, key: int) -> int:
        if key in self.d:
            self.q.pop(self.q.index(key))
            self.q.append(key)
            # print(self.q, self.d)
            return self.d[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.q.pop(self.q.index(key))
            self.q.append(key)
            self.d[key] = value
        else:
            var = self.q.pop(0)
            if var != -1:
                del self.d[var]
            self.q.append(key)
            self.d[key] = value
            # print(self.q, self.d)
