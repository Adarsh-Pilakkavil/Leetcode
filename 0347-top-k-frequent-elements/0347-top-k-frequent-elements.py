class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            if nums[i] in d.keys():
                d[nums[i]]+=1
            else:
                d[nums[i]]=1
        d=dict(sorted(d.items(),key=lambda item: item[1],reverse=True))
        count=0
        l=[]
        for i in d.keys():
            if count!=k:
                l.append(i)
                count+=1
            else:
                break
        return l
