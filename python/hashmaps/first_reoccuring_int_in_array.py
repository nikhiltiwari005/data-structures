arr = [4,1,8,5,5,6,3,8,4,3]


def findReoccurringElementInArr(arr: list) -> int:
    freq = {}
    
    for i in arr:
        if i in freq:
            return i
        freq[i] = 1
    return None

print(findReoccurringElementInArr(arr))