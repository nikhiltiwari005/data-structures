

class CustomArray:
    
    def __init__(self):
        self.data = {}
        self.len = 0      
    
    def push(self, obj) -> bool:
        self.data[self.len] = obj
        self.len += 1
        return True
        
    def pop(self, index = None) -> bool:
        index = self.len - 1 if index is None else index
        self.remove(index)
        return True
        
    def get(self, index):
        if index > self.len:
            raise Exception("Index not found")
        return self.data[index]
    
    def remove(self, index):
        if self.len <= 0:
            raise Exception("Array is empty")
        if index >= self.len:
            raise Exception("Index not found")
        
        i = index
        while i < (self.len - 1):
            self.data[i] = self.data[i+1]
            i += 1
            
        del self.data[self.len - 1]
        self.len -= 1
        
    def insert(self, index, newVal):
        if self.len <= 0:
            raise Exception("Array is empty")
        if index >= self.len:
            raise Exception("Index not found")
        
        while index <= (self.len - 1):
            oldVal = self.data[index]
            self.data[index] = newVal
            newVal = oldVal
            index += 1
        
        self.push(newVal)
        
    def replace(self, index, newVal):
        self.data[index] = newVal
        
            
    def __str__(self):
        print(self.data, self.len)
        return ""
        
arr = CustomArray()
arr.push("a")
arr.push("b")
arr.push("c")
print(arr)
arr.pop(1)
print(arr)
arr.insert(1, "B")
print(arr)
arr.pop()
print(arr)
