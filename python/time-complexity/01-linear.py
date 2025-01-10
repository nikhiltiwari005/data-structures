from memory_profiler import profile

print("Linear TX \n")

names = ["john", "sam", "raj"]

@profile
def printNames(list):
    print("No of persons", len(list))
    for index, name in enumerate(names):
        print(index + 1, str.capitalize(name))


printNames(names)