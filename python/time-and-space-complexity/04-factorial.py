from itertools import permutations

print("Factorial Time Complexity Examples (O(n!))\n")

# Example 1: Generating All Permutations of a List
def generate_permutations(arr):
    print("Example 1: Generating All Permutations")
    perms = list(permutations(arr))  # Generate all permutations
    for perm in perms:
        print(perm)
    print(f"Total permutations: {len(perms)}")
    print("-" * 30)

generate_permutations([1, 2, 3])


# Example 2: Recursive Permutations
def recursive_permutations(arr, path=[]):
    if not arr:
        print(path)
        return
    
    for i in range(len(arr)):
        recursive_permutations(arr[:i] + arr[i+1:], path + [arr[i]])

print("Example 2: Recursive Permutations")
recursive_permutations([1, 2, 3])
print("-" * 30)


# Example 3: Generating All Possible Arrangements of Letters
def letter_arrangements(string):
    print("Example 3: Generating All Letter Arrangements")
    def helper(s, path=""):
        if not s:
            print(path)
            return
        for i in range(len(s)):
            helper(s[:i] + s[i+1:], path + s[i])
    
    helper(string)
    print("-" * 30)

letter_arrangements("abc")


# Example 4: Solving the Traveling Salesman Problem (TSP) Brute Force
def traveling_salesman(cities):
    print("Example 4: Traveling Salesman Problem Brute Force")
    min_distance = float('inf')
    best_path = None
    
    for path in permutations(cities):  # All possible orderings of cities
        distance = sum(abs(path[i] - path[i-1]) for i in range(1, len(path)))
        if distance < min_distance:
            min_distance = distance
            best_path = path
    
    print(f"Shortest Path: {best_path} with distance: {min_distance}")
    print("-" * 30)

traveling_salesman([1, 3, 6, 8, 12])


# Example 5: Generating All Subsets (Power Set) with Order
def generate_subsets_with_order(arr):
    print("Example 5: Generating All Subsets with Order")
    all_subsets = []
    for r in range(1, len(arr) + 1):
        subsets = list(permutations(arr, r))
        all_subsets.extend(subsets)
    
    for subset in all_subsets:
        print(subset)
    print(f"Total ordered subsets: {len(all_subsets)}")
    print("-" * 30)

generate_subsets_with_order([1, 2, 3])