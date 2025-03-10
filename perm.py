
def generate_permutations(nums, path=[], used=None):
    if used is None:
        used = [False] * len(nums)  # Track which elements are used

    if len(path) == len(nums):  # Base case: full permutation
        print(path)  # Print or store the permutation
        return

    for i in range(len(nums)):
        if not used[i]:  # If nums[i] is not already used
            used[i] = True  # Mark as used
            print(used)
            generate_permutations(nums, path + [nums[i]], used)  # Recursive call
            used[i] = False  # Undo choice (backtrack)
            print(used)
# Example usage
generate_permutations([1, 2, 3])
