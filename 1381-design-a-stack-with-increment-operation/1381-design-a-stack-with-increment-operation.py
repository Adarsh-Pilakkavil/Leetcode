class CustomStack:

    def __init__(self, maxSize: int):
        self.arr=[]
        self.maxi=maxSize
        self.length=0
    def push(self, x: int) -> None:
        if self.length==self.maxi:
            return 
        self.length+=1
        self.arr.append(x)
    def pop(self) -> int:
        if self.length==0:
            return -1
        self.length-=1
        return self.arr.pop()
    def increment(self, k: int, val: int) -> None:
        if self.length<=k:
            for i in range(self.length):
                self.arr[i]+=val
        else:
            for i in range(k):
                self.arr[i]+=val
# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)