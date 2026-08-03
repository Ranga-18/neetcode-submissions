class Solution:
    def reverse(self, x: int) -> int:
        k=abs(x)
        n=0
        while k>0:
            n=n*10+k%10
            k//=10
        limit=2**31
        if x<0:
            if -n<-limit: return 0
            else:
                return -n
        return 0 if n>limit-1 else n