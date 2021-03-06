class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []
        self.front = None
        self.n = 0

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if self.n == 0:
            self.front = x
        self.s1.append(x)
        self.n += 1

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        for i in range(self.n - 1, -1, -1):
            self.s2.append(self.s1.pop(i))
        temp = self.s2.pop(self.n - 1)
        self.n -= 1
        for i in range(self.n - 1, -1, -1):
            self.s1.append(self.s2.pop(i))
        if self.n > 0:
            self.front = self.s1[0]
        return temp

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.front

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if self.n == 0:
            return True
        else:
            return False

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()