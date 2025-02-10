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
            self.append(value)
            return
        
        firstNode = self.head
        newNode = Node(value)
        if index == 0:
            self.head = newNode
            newNode.next = firstNode
            self.length += 1
            return
        
        firstNode = self.traverseToIndex(index)
    
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
        
        firstNode = self.traverseToIndex(index)
        
        firstNode.next = firstNode.next.next
        
        if index == self.length-1:
            self.tail = firstNode
            
        self.length -= 1
        return self

    def printList(self):
        arr = []
        current = self.head
        while current is not None:
            arr.append(current.value)
            current = current.next
            
        return arr
    
    def traverseToIndex(self, index):
        firstNode = self.head
        i = 0
        while i < index - 1:
            fn = firstNode.next
            firstNode = fn
            i += 1
        
        return firstNode

    def reverseList(self):        
        curr = tail = self.head
        pre = None
        while curr:
            next_node = curr.next
            curr.next = pre
            pre = curr
            curr = next_node
        self.head = pre
        self.tail = tail
        return self

ll = LinkedList(5)
ll.append(10)
ll.append(15)
ll.append(20)
# print(ll.printList())
# ll.insert(0, 0)
# print(ll.printList())
# ll.remove(4)
# print(ll.printList())
# ll.remove(2)
# print(ll.printList())
print(ll.printList())
ll.reverseList()
print(ll.printList())
    
    