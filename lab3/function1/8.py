def spy_game(nums):
    pattern = [0, 0, 7]
    index = 0
    for num in nums:
        if num == pattern[index]:
            index += 1
            if index == len(pattern):
                return True
    return False

# Example usage:
print(spy_game([1, 2, 4, 0, 0, 7, 5]))  # True
print(spy_game([1, 7, 2, 0, 4, 5, 0]))  # False
