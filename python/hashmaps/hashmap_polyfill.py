
class CustomHashMap:
    
    def __init__(self, size):
        self.size = size
        self.data = []
        for i in range(size):
            self.data.append([])
        
    def _hash(self, key: str):
        num_string = ""
        for k in key:
            num_string += str(ord(k))
            
        return int(num_string) % self.size
    
    def set(self, key, value):
        index = self._hash(key)
        print(self.data[index].extend([[key, value]]))

    def get(self, key):
        arr = self.data[self._hash(key)]
        for pair in arr:
            if(key == pair[0]):
                return pair[1]
    
chm = CustomHashMap(10)
chm.set("hi", "hello")
chm.set("hii", "helloo")
chm.set("hiiiiii", "hellooooooo")
chm.set("my", "MYY")

print(chm.get("hii"))