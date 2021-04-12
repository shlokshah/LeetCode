class stack:
    def __init__(self):
        self.s=[]

    def push(self, val):
        if len(self.s)==0:
            self.s.append(val)
        else:
            temp=[]
            while len(self.s)>0 and val>self.s[-1]:
                temp.append(self.s.pop(-1))
            self.s.append(val)
            while len(temp)!=0:
                self.s.append(temp.pop(-1))

    def pop(self):
        return self.s.pop(-1)

    def peek(self):
        return self.s[-1]

    def isEmpty(self):
        return len(self.s)==0

    def display(self):
        print('Top->', end="")
        for i in self.s[::-1]:
            print(str(i)+'->', end="")
        print('|')

if __name__ == '__main__':
    A=stack()
    A.push(4)
    A.push(2)
    A.push(1)
    A.display()
    A.push(8)
    A.display()
    print(A.pop())
    A.display()
    print(A.peek())
    A.display()
    print(A.isEmpty())