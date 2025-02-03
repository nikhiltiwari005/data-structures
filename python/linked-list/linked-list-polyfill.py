class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1
    
    def append(self, value):
        newNode = Node(value)
        self.tail.next = newNode
        self.tail = newNode
        self.length += 1
        return self
    
    def prepend(self, value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode
        self.length += 1
        return self
    
    def insert(self, index, value):
        if index >= self.length:
            raise Exception("Index doesn't exist")
        
        firstNode = self.head
        newNode = Node(value)
        if index == 0:
            self.head = newNode
            newNode.next = firstNode
            self.length += 1
            return
        
        i = 0
        while i < index - 1:
            fn = firstNode.next
            firstNode = fn
            i += 1
            
        sn = firstNode.next
        newNode.next = sn
        firstNode.next = newNode
        self.length += 1
        return self
    
    def remove(self, index):
        if index >= self.length:
            raise Exception("Index doesn't exist")
        
        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return
        
        firstNode = self.head
        i = 0
        while i < index - 1:
            fn = firstNode.next
            firstNode = fn
            i += 1
        
        firstNode.next = firstNode.next.next
        
        if index == self.length-1:
            self.tail = firstNode
            
        self.length -= 1
        return self


ll = LinkedList(5)
ll.append(10)
ll.append(15)
ll.append(20)
ll.insert(0, 0)
ll.remove(4)

print(ll)
    
    