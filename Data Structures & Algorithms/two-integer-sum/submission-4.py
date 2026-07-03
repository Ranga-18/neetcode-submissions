class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d=Counter(nums)
        for i in range(len(nums)):
            remain=target-nums[i]
            if remain in d:
                if remain==nums[i] and d[remain]>1:
                    return [i,nums[i+1:].index(remain)+i+1]
                elif remain!=nums[i]:
                    return [i,nums.index(remain)]