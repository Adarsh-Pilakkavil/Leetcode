class Solution:
    def minMoves(self, nums: List[int]) -> int:
        ma,mi=max(nums),min(nums)
        cma,cmi=1,1
        if ma==mi:
            return 0
        c=ma-mi
        t=0
        for i in range(len(nums)):
            if nums[i]==ma:
                if cma==1:
                    cma-=1
                    continue
                else:
                    t+=(c+nums[i])-ma
            elif nums[i]==mi:
                if cmi==1:
                    cmi-=1
                    continue
                else:
                    t+=(c+nums[i])-ma
            else:
                t+=(c+nums[i])-ma
        return t+c
