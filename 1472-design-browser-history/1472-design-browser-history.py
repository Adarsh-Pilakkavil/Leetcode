class BrowserHistory:

    def __init__(self, homepage: str):
        self.f=[]
        self.stack=list()
        self.stack.append(homepage)
    def visit(self, url: str) -> None:
        self.stack.append(url)
        self.f=[]
    def back(self, steps: int) -> str:
        while len(self.stack)!=1 and steps:
            self.f.append(self.stack.pop())
            steps-=1
        return self.stack[-1]
    def forward(self, steps: int) -> str:
        while self.f and steps:
            self.stack.append(self.f.pop())
            steps-=1
        return self.stack[-1]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)