from itertools import permutations
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if s1 in s2:
            return True
        t1,t2=set(s1),set(s2)
        for i in t1:
            if i in t2:
                continue
            else:
                return False
        p=list(permutations(s1))
        for i in p:
            if ''.join(i) in s2:
                return True
        return False