class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        ans=[0]*n
        if n==1: return ans
        for i in range(n):
            for j in range(i+1,n):
                if temperatures[j]>temperatures[i]:
                    ans[i]=j-i
                    break

        
        return ans