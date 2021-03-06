class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = []
        self.q2 = []
        self.topEle = None
        self.n = 0

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q1.append(x)
        self.topEle = x
        self.n += 1

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        old_top = self.topEle
        self.topEle = self.q1[self.n - 2]
        for i in range(self.n - 1):
            self.q2.append(self.q1[i])
        self.n -= 1
        self.q1 = self.q2
        return old_top

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.topEle

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if self.n == 0:
            return True
        else:
            return False

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()