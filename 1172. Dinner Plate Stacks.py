# class stack:
#     def __init__(self):
#         self.next=None
#         self.stack=[]
#
# class DinnerPlates:
#     def __init__(self, capacity: int):
#         self.plates=stack()
#         self.head=self.tail=self.plates
#         self.count=0
#         self.thres=capacity
#
#
#     def push(self, val: int) -> None:
#         if self.count<self.thres:
#             self.tail.stack.append(val)
#             self.count+=1
#         else:
#             new=stack()
#             self.tail.next=new
#             self.tail=new
#             self.tail.stack.append(val)
#             self.count+=1
#
#
#     def pop(self) -> int:
#
#     def popAtStack(self, index: int) -> int:
#
# # Your DinnerPlates object will be instantiated and called as such:
# # obj = DinnerPlates(capacity)
# # obj.push(val)
# # param_2 = obj.pop()
# # param_3 = obj.popAtStack(index)