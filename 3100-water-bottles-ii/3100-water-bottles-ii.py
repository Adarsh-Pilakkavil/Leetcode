class Solution(object):
    def maxBottlesDrunk(self, numBottles, numExchange):
        def numWaterBottles(numBottles, numExchange):
            total = numBottles
            empty = numBottles
            new_full=0
            while empty+new_full >= numExchange:
                total += 1
                new_full+=1
                empty-=numExchange
                numExchange+=1
            return total
        return numWaterBottles(numBottles,numExchange)
        