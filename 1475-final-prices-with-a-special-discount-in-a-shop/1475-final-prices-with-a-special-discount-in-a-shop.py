class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        k=[]
        for i in range(len(prices)):
            c=0
            for j in range(i+1,len(prices)):
                if prices[i]>=prices[j]:
                    k.append(prices[i]-prices[j])
                    c=1
                    break
            if c==0:
                k.append(prices[i])
        return k

