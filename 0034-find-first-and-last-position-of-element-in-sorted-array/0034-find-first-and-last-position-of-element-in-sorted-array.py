class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bound(f):
            l,r=0,len(nums)-1
            b=-1
            while l<=r:
                mid=(l+r)//2
                if nums[mid]==target:
                    b=mid
                    if f:
                        r=mid-1
                    else:
                        l=mid+1
                elif nums[mid]>target:
                    r=mid-1
                else:
                    l=mid+1
            return b
        start=bound(True)
        finish=bound(False)
        return [start,finish]