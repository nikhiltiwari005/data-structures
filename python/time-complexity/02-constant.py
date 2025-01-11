print("Constant Time Complexity")

print("Constant Time Complexity Example 1")
def constantEx1(num1: int, num2: int):
    return num1 + num2

print("Sum:", constantEx1(1, 2))


print("Constant Time Complexity Example 2")
def constantEx2(num1: int, num2: int):
    return num1 - num2

print("Subtraction:", constantEx2(2, 1))


print("Constant Time Complexity Example 3")
def constantEx3(numList: list):
    if len(numList) < 2:
        raise Exception("Invalid input")
    return numList[0] + numList[1]

print("Sum of first 2 indices:", constantEx3([1, 2, 3, 4, 5]))


print("Constant Time Complexity Example 4")
def constantEx4(numList: list):
    if len(numList) < 10:
        raise Exception("Invalid input")
    return numList[5] + numList[8] + numList[0]

print("Sum of 3 random indices:", constantEx4([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))


print("Constant Time Complexity Example 5")
def constantEx5(numList: list):
    if len(numList) < 3:
        raise Exception("Invalid input")
    return numList[0] + numList[1] + numList[2]

print("Sum of first 3 indices:", constantEx5([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))


print("Constant Time Complexity Example 6")
def access_element(lst, index):
    if index >= len(lst):
        raise Exception("Index out of range")
    return lst[index]

print("Access specific element:", access_element([10, 20, 30, 40, 50], 3))


print("Constant Time Complexity Example 7")
def assign_variable():
    x = 42
    y = "hello"
    z = 3.14
    return x, y, z

print("Assigned variables:", assign_variable())


print("Constant Time Complexity Example 8")
def is_even(num):
    return num % 2 == 0

print("Is 10 even?:", is_even(10))
print("Is 7 even?:", is_even(7))


print("Constant Time Complexity Example 9")
def swap(a, b):
    a, b = b, a
    return a, b

x, y = swap(3, 5)
print("Swapped values:", x, y)


print("Constant Time Complexity Example 10")
def first_and_last(lst):
    if not lst:
        raise Exception("List is empty")
    return lst[0], lst[-1]

print("First and last element:", first_and_last([1, 2, 3, 4, 5]))


print("Constant Time Complexity Example 11")
def is_empty(lst):
    return len(lst) == 0  # Or simply `return not lst`

print("Is the list empty?:", is_empty([]))
print("Is the list empty?:", is_empty([1, 2]))


print("Constant Time Complexity Example 12")
def get_pi():
    return 3.14159

print("PI value:", get_pi())


print("Constant Time Complexity Example 13")
def logical_operations(a, b):
    return a and b, a or b, not a

print("Logical operations:", logical_operations(True, False))


print("Constant Time Complexity Example 14")
def check_membership(s, value):
    return value in s

my_set = {1, 2, 3, 4, 5}
print("Is 3 in the set?:", check_membership(my_set, 3))
print("Is 6 in the set?:", check_membership(my_set, 6))


print("\nTime complexity and space complexity of all the above are O(1)")


def ts(numList: list):
    toReturn = 0
    
    for i, num in enumerate(numList):
        if i >= 1000000000000000000:
            break
        
        toReturn += num
        
    return toReturn

print("this is O(n)", ts([1,2,3,4,5,6,7,8,9, 0]))
