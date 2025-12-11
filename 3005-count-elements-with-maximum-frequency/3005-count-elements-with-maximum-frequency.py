class Solution(object):
    def maxFrequencyElements(self, nums):
        freq={}
        for i in nums:
            freq[i]=freq.get(i,0)+1
        maxi=max(freq.values())
        cnt=0
        for v in freq.values():
            if v==maxi:
                cnt+=v
        return cnt
        