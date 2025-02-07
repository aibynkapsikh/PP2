def unique_list(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

# Example usage:
print(unique_list([1, 2, 2, 3, 4, 4, 5]))  # Output: [1, 2, 3, 4, 5]
