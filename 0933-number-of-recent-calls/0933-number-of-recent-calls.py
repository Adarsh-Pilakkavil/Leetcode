class RecentCounter:

    def __init__(self):
        self.counter=[]
    def ping(self, t: int) -> int:
        self.counter.append(t)
        c=len(self.counter)-1
        while c!=-1 and self.counter[c]>=t-3000:
            c-=1
        return len(self.counter)-c-1
# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)