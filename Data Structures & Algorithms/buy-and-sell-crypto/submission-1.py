class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # best=0
        # for i in range(len(prices)-1):
        #     curr=max(prices[i+1:])-prices[i]
        #     if best<curr:
        #         best=curr
        # return best
        buy=float('inf')
        m=0
        for p in prices:
            if buy>p:
                buy=p
            else:
                m=max(m,p-buy)
        return m
# prices = [10,1,5,6,7,1]