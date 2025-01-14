arr1 = [0,3,4,31,32]
arr2 = [4,6,30,34]

def mergeSortedArray(arr1, arr2):
    
    if not arr1 and not arr2:
        raise Exception("empty inputs")
    if not arr1:
        return arr2  
    if not arr2:
        return arr1
    
    mergedArr = []
    i = 0
    j = 0
    
    while i < len(arr1) and j < len(arr2):
        
        if arr1[i] < arr2[j]:
            mergedArr.append(arr1[i])
            i += 1
        else:
            mergedArr.append(arr2[j])
            j += 1
            
    while i < len(arr1):
        mergedArr.append(arr1[i])
        i += 1

    while j < len(arr2):
        mergedArr.append(arr2[j])
        j += 1
    
    return mergedArr

print(mergeSortedArray(arr1, arr2))

