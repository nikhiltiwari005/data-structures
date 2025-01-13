

class CustomArray:
    
    def __init__(self):
        self.data = {}
        self.len = 0      
    
    def push(self, obj) -> bool:
        self.data[self.len] = obj
        self.len += 1
        return True
        
    def pop(self) -> bool:
        self.remove(self.len)
        return True
        
    def get(self, index):
        if index > self.len:
            raise Exception("Index not found")
        return self.data[index]
    
    def remove(self, index):
        i = index
        while i < self.len - 1:
            self.data[i] = self.data[i+1]
            i += 1
            
        del self.data[self.len - 1]
        self.len -= 1
            
    def __str__(self):
        print(self.data, self.len)
        return ""
        
arr = CustomArray()
arr.push("a")
arr.push("b")
arr.push("c")
print(arr)
arr.pop()
print(arr)
