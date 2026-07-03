class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c=Counter(nums).most_common()[:k]
        return [c[i][0] for i in range(len(c))]