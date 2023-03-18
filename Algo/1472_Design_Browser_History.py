class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = []
        self.future = []
        self.cur = homepage

    def visit(self, url: str) -> None:
        self.history.append(self.cur)
        self.cur = url
        self.future = []

    def back(self, steps: int) -> str:
        while steps > 0 and self.history:
            self.future.append(self.cur)
            self.cur = self.history.pop()
            steps -= 1
        return self.cur

    def forward(self, steps: int) -> str:
        while steps > 0 and self.future:
            self.history.append(self.cur)
            self.cur = self.future.pop()
            steps -= 1
        return self.cur


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
