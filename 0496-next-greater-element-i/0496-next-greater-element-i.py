class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s=[]
        d={}
        nums2.append(-1)
        res=[]
        for num in nums2:
            while s and (s[-1]<num or num==-1):
                c=s.pop()
                d[c]=num
            s.append(num)
        for i in nums1:
            res.append(d[i])
        return res
            
            