from math import floor,ceil
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk =[]
        for i in tokens:
            if i in '+-*/':
                b,a = stk.pop(),stk.pop()
                if i=='+':
                    stk.append(a+b)
                elif i=='-':
                    stk.append(a-b)
                elif i=='*':
                    stk.append(a*b)
                else:
                    d = a/b
                    if d<0:
                        stk.append(ceil(d))
                    else:
                        stk.append(floor(d))
            else:
                stk.append(int(i))
        return stk[0]