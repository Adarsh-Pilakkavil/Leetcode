class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        t=set()
        for i in range(len(nums)-2):
            if i>0 and nums[i]== nums[i-1]:
                continue
            firstnum=nums[i]
            j,k=i+1,len(nums)-1
            while j<k:
                secondnum,thirdnum=nums[j],nums[k]
                p=firstnum+secondnum+thirdnum
                if p>0:
                    k-=1
                elif p<0:
                    j+=1
                else:
                    t.add((firstnum,secondnum,thirdnum))
                    j,k=j+1,k-1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                    while j<k and nums[k]==nums[k+1]:
                        k-=1
        return list(t)