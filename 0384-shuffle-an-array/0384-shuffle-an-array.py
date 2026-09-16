class Solution:

    def __init__(self, nums: list[int]):
        self.a=nums[:]
        self.d=nums[:]
        self.l=len(self.d)
    def reset(self) -> list[int]:
        self.d=self.a[:]
        return self.d

    def shuffle(self) -> list[int]:
        arr=self.d[:]
        for i in range(self.l):
            j=randint(i,self.l-1)
            arr[i],arr[j]=arr[j],arr[i]
        return arr

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()