arr = [4,2,4,4]
sum = 6

def hasTwoPairSum(arrList: list, sum: int) -> bool:
    uniqueEle = set()
    for val in arrList:
        if val in uniqueEle:
            return True
        uniqueEle.add(sum - val)
        print(uniqueEle)
    
    return False

print(hasTwoPairSum(arr, sum))
