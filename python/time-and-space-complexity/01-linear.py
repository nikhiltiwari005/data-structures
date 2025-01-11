import os

print("Linear Time complexity \n")

names = ["john", "sam", "raj"]

print("Linear Time complexity Example 1")

def linearEx1(list):
    x = newArr()
    print(x)
    print("No of persons", len(list))
    for index, name in enumerate(names):
        print(index + 1, str.capitalize(name))

def newArr():
    return [1, "r"]

linearEx1(names)


print("\n\nLinear Time complexity Example 2")

def linearEx2(userList: list):
    i = 0
    userLen = len(userList)
    while userLen > i:
        print(i + 1, userList[i])
        i += 1
        
linearEx2(names)

print(os.linesep, "\nLinear Time complexity Example 3")

def linearEx3(users: list):
    i = 1
    for name in users:
        print(i, name)
        i += 1

    print("-----------")
    i = 1
    for name in enumerate(users):
        print(i, name)
        i += 1
    
    print("-----------")
    for name in enumerate(users):
        print(name[0] + 1, name[1])
        
linearEx3(names)


print("Time Complexity of all 3 programs are O(n), Space Complexity is O(1)")