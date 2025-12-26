class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s=[]
        i=0
        res=[-1]*len(nums1)
        while i!=len(nums2):
            if s and nums2[i]>nums2[s[-1]]:
                k=nums1.index(nums2[s.pop()])
                res[k]=nums2[i]
                continue
            if nums2[i] in nums1:
                s.append(i)
            i+=1
        return res
            
            