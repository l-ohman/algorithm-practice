# https://leetcode.com/problems/insert-delete-getrandom-o1/?envType=daily-question&envId=2024-01-16

from random import randint

class RandomizedSet:

    def __init__(self):
        self.set = set()
        

    def insert(self, val: int) -> bool:
        if val in self.set:
            return False
        self.set.add(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val in self.set:
            self.set.remove(val)
            return True
        return False
        

    def getRandom(self) -> int:
        return list(self.set)[randint(0, len(self.set)-1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()