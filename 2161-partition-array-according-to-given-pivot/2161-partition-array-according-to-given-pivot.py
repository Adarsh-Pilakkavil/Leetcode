class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        a,b,c=[],0,[]
        for i in range(len(nums)):
            if nums[i]>pivot:
                c.append(nums[i])
            elif nums[i]<pivot:
                a.append(nums[i])
            else:
                b+=1
        return a+b*[pivot]+c