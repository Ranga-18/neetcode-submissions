class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {')' : '(', '}' : '{', ']' : '['}
        stk = []
        for ch in s:
            if ch not in hashmap:
                stk.append(ch)
            else:
                if not stk: return False
                else:
                    popped = stk.pop()
                    if popped!=hashmap[ch]:
                        return False
        return not stk