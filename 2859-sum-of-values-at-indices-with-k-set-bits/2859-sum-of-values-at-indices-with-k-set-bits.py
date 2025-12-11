class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        sum=0
        for i in range(0, len(nums),1):
            if bin(i)[2:].count("1")==k:
                sum+=nums[i]
        return sum