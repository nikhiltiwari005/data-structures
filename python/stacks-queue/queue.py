
# class Node:
    
#     def __init__(self, value):
#         self.value = value
#         self.next = None
        
# class Queue:
    
#     def __init__(self):
#         self.first = None
#         self.last = None
#         self.length = 0
        
#     def peek(self):
#         return self.first.value if self.first else None        
    
#     def enqueue(self, value):
#         newNode = Node(value)
#         if self.length == 0:
#             self.first = newNode
#             self.last = newNode
#         else:
#             self.last.next = newNode
#             self.last = newNode
#         self.length += 1
    
#     def dequeue(self):
#         if not self.first:
#             return None
        
#         first = self.first
#         self.first = self.first.next
#         self.length -= 1
#         first.next = None
#         if self.length == 0:
#             self.last = None
            
#         return first.value
        
#     def isempty(self):
#         return self.length == 0 
    

# q = Queue()
# q.enqueue("a")
# print(q.peek())
# q.enqueue("b")
# print(q.peek())
# q.enqueue("c")
# print(q.peek())
# print("-----------------")
# print(q.dequeue())
# print(q.dequeue())
# print(q.dequeue())
# print(q.dequeue())


class QueueStack:
    
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def enqueue(self, value):
        self.stack1.append(value)
        print(self.stack1)
        print(self.stack2)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop() if self.stack2 else None

    def peek(self):
        if self.stack2:
            return self.stack2[-1]
        if self.stack1:
            return self.stack1[0]
        
    



qq = QueueStack()
qq.enqueue(1)
qq.enqueue(2)
qq.enqueue(3)

qq.dequeue()
qq.enqueue(4)
qq.enqueue(5)
qq.enqueue(6)
qq.dequeue()
qq.enqueue(7)
qq.dequeue()
qq.dequeue()
qq.enqueue(8)


print(qq.peek())