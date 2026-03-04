import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def qs(nums,k):
            pivot=random.choice(nums)
            left,mid,right=[],[],[]
            for i in nums:
                if i>pivot:
                    left.append(i)
                elif i<pivot:
                    right.append(i)
                else:
                    mid.append(i)
            if len(left)>=k:
                return qs(left,k)
            if len(left)+len(mid)<k:
                return qs(right,k-len(left)-len(mid))
            return pivot
        return qs(nums,k)