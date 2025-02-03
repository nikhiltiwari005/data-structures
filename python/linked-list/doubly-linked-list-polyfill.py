class Node:
    def __init__(self, value, nextNode=None, previousNode=None):
        self.value = value
        self.next = nextNode
        self.previous = previousNode

class DoublyLinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def append(self, value):
        newNode = Node(value, previousNode=self.tail)
        self.tail.next = newNode
        self.tail = newNode
        self.length += 1
        return self

    def prepend(self, value):
        newNode = Node(value)
        self.head.previous = newNode
        newNode.next = self.head
        self.head = newNode
        self.length += 1
        return self

    def insert(self, index, value):
        if index >= self.length:
            self.append(value)
            return

        if index == 0:
            newNode = Node(value, nextNode=self.head)
            newNode.next.previous = newNode
            self.head = newNode
            self.length += 1
            return

        currentNode = self.traverseToIndex(index)
        newNode = Node(value, currentNode.next, currentNode)
        currentNode.next.previous = newNode
        currentNode.next = newNode
        self.length += 1
        return self

    def remove(self, index):
        if index > self.length:
            raise Exception("Index doesn't exist")

        if index == 0:
            self.head = self.head.next
            self.head.previous = None
            self.length -= 1
            return
        
        if index == self.length:
            self.tail = self.tail.previous
            self.tail.next = None
            self.length -= 1
            return

        firstNode = self.traverseToIndex(index)

        firstNode.next = firstNode.next.next
        firstNode.next.previous = firstNode

        self.length -= 1
        return self

    def traverseToIndex(self, index):
        firstNode = self.head
        i = 0
        while i < index - 1:
            fn = firstNode.next
            firstNode = fn
            i += 1

        return firstNode

    def printList(self):
        arr = []
        current = self.head
        while current is not None:
            arr.append(current.value)
            current = current.next

        arr.append("<->")

        current = self.tail
        while current is not None:
            arr.append(current.value)
            current = current.previous

        return arr

ll = DoublyLinkedList(5)
ll.append(10)
ll.append(15)
ll.append(20)
print(ll.printList())
ll.insert(0, 0)
print(ll.printList())
ll.insert(2, 4)
print(ll.printList())
ll.remove(4)
print(ll.printList())
