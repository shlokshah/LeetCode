class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.s = []
        self.n = 0

    def push(self, x: int) -> None:
        if self.n < self.maxSize:
            self.s.append(x)
            self.n += 1

    def pop(self) -> int:
        if self.n > 0:
            temp = self.s.pop(self.n - 1)
            self.n -= 1
            return temp
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        if self.n > k:
            for i in range(k):
                self.s[i] = self.s[i] + val
        else:
            for i in range(self.n):
                self.s[i] = self.s[i] + val

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)