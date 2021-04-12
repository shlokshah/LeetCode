class node:
    def __init__(self, type):
        self.type=type
        self.next=None

class AnimalShelter:
    def __init__(self):
        self.head=None
        self.tail=None
    def enqueue(self, type):
        if self.head==None:
            new=node(type)
            new.next=None
            self.head=self.tail=new
        else:
            new=node(type)
            new.next=None
            self.tail.next=new
            self.tail=new
    def dequeue(self, type=None):
        if type==None or self.head.type==type:
            cur=self.head
            self.head=self.head.next
            return cur.type
        else:
            back=self.head
            front=self.head.next
            while front.type!=type:
                back=back.next
                front=front.next
            back.next=front.next
            return front.type
    def display(self):
        cur=self.head
        while cur!=None:
            print(cur.type+'->', end="")
            cur=cur.next
        print('|')

if __name__ == '__main__':
    A=AnimalShelter()
    A.enqueue('dog')
    A.enqueue('dog')
    A.enqueue('cat')
    A.enqueue('dog')
    A.enqueue('cat')
    A.display()
    print(A.dequeue())
    A.display()
    print(A.dequeue('cat'))
    A.display()