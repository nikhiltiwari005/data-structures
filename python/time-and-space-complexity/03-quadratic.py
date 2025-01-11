# Quadratic Time Complexity Examples (O(n²))

print("Quadratic Time Complexity Examples\n")

def quadraticEx1(numList: list):
    for v in numList:
        for vv in numList:
            print(v, "X", vv, "=", v * vv)
        print("-----")            


quadraticEx1([1,2,3,4,5,6,7,8,9,10])

# Example 1: Finding Duplicate Pairs
def find_duplicate_pairs(num_list):
    print("Example 1: Duplicate Pairs")
    for i in range(len(num_list)):  # Outer loop
        for j in range(i + 1, len(num_list)):  # Inner loop
            if num_list[i] == num_list[j]:  # Check for duplicates
                print(f"Duplicate pair found: ({num_list[i]}, {num_list[j]})")
    print("-" * 30)

find_duplicate_pairs([1, 2, 3, 2, 4, 1])


# Example 2: Matrix Multiplication
def matrix_multiply(matrix1, matrix2):
    print("Example 2: Matrix Multiplication")
    rows = len(matrix1)
    cols = len(matrix2[0])
    common = len(matrix2)
    result = [[0 for _ in range(cols)] for _ in range(rows)]
    
    for i in range(rows):  # Outer loop for rows in matrix1
        for j in range(cols):  # Inner loop for columns in matrix2
            for k in range(common):  # Multiply and sum elements
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    
    for row in result:
        print(row)
    print("-" * 30)

matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]
matrix_multiply(matrix1, matrix2)


# Example 3: Bubble Sort
def bubble_sort(arr):
    print("Example 3: Bubble Sort")
    n = len(arr)
    for i in range(n):  # Outer loop
        for j in range(0, n - i - 1):  # Inner loop to compare adjacent elements
            if arr[j] > arr[j + 1]:  # Swap if necessary
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print("Sorted Array:", arr)
    print("-" * 30)

bubble_sort([64, 34, 25, 12, 22, 11, 90])


# Example 4: Finding All Pairs of Indices
def all_pairs(arr):
    print("Example 4: All Pairs of Indices")
    pairs = []
    for i in range(len(arr)):  # Outer loop
        for j in range(len(arr)):  # Inner loop
            pairs.append((i, j))  # Add every possible pair of indices
    print("All Pairs:", pairs)
    print("-" * 30)

all_pairs([1, 2, 3])


# Example 5: Counting Inversions in an Array
def count_inversions(arr):
    print("Example 5: Counting Inversions")
    inversions = 0
    for i in range(len(arr)):  # Outer loop
        for j in range(i + 1, len(arr)):  # Inner loop for pairs
            if arr[i] > arr[j]:
                inversions += 1
    print("Total Inversions:", inversions)
    print("-" * 30)

count_inversions([2, 4, 1, 3, 5])


# Example 6: Checking All Subarray Sums
def subarray_sums(arr):
    print("Example 6: Subarray Sums")
    sums = []
    for i in range(len(arr)):  # Outer loop for starting index
        total = 0
        for j in range(i, len(arr)):  # Inner loop for ending index
            total += arr[j]  # Add current element
            sums.append(total)  # Store subarray sum
    print("Subarray Sums:", sums)
    print("-" * 30)

subarray_sums([1, 2, 3])