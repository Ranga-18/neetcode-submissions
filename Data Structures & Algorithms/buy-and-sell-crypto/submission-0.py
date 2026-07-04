class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best=0
        for i in range(len(prices)-1):
            curr=max(prices[i+1:])-prices[i]
            if best<curr:
                best=curr
        return best
