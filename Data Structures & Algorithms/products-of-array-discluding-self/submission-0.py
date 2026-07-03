class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product=1
        for i in nums:
            product*=i
        if 0 in nums:
            if nums.count(0)>1:
                return [0]*len(nums)
            else:
                temp=[0]*len(nums)
                index=nums.index(0)
                nums.remove(0)
                product=1
                for i in nums:
                    product*=i
                temp[index]=product
                return temp
        else:
            for i in range(0,len(nums)):
                nums[i]=product//nums[i]
            return nums