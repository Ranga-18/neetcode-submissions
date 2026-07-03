class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d={}
        for i,val in enumerate(numbers):
            remain=target-val
            if remain in d:
                return [d[remain],i+1]
            d[val]=i+1
        