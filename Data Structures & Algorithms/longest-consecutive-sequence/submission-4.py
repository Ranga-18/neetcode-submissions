class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        s={}
        nums.sort()
        for i in nums:
            if i-1 in s:
                s[i]=s[i-1]+1
            else:
                s[i]=1
        return max(s.values())