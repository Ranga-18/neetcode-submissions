class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[1]*n
        prefix=1
        suffix=1
    
        for i in range(n):
            ans[i]*=prefix
            prefix*=nums[i]
        #suffix=1
        #for i in range(n-1,-1,-1):
            ans[n-i-1]*=suffix
            suffix*=nums[n-i-1]
        
        return ans