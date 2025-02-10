class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        # self.previous

# Last in, Last out. (LIFO)      
class StackLinkedList:
    
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0
    
    def push(self, value):
        newNode = Node(value)
        if self.top is None:
            self.top = newNode
            self.bottom = newNode
        else:
            newNode.next = self.top
            self.top = newNode
        self.length += 1        
    
    def pop(self) -> str:
        if self.top is None:
            return None
        if self.top == self.bottom:
            self.bottom = None
        popped = self.top
        self.top = popped.next
        popped.next = None
        self.length -= 1
        return popped.value
    
    def peek(self) -> str:
        if self.top is None:
            return None
        return self.top.value
    
print("Stack using linked list")

stack = StackLinkedList()
stack.push("a")
print(stack.peek())
stack.push("b")
print(stack.peek())
stack.push("c")
print(stack.peek())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())

print("=" * 10)

print("Stack using array")

class StackArray:
    
    def __init__(self):
        self.arr = []
    
    def push(self, value):
        self.arr.append(value)
    
    def pop(self):
        return self.arr.pop() if self.arr else None
    
    def peek(self):
        return self.arr[-1] if self.arr else None
    
stack = StackArray()
stack.push("a")
print(stack.peek())
stack.push("b")
print(stack.peek())
stack.push("c")
print(stack.peek())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())