# Problem: Given an array of sorted numbers and a target sum,
# find a pair in the array whose sum is equal to the given target

def find_pair_with_target_sum(arr, target_sum):
    numbers = {}  # store numbers and indices
    for index, num in enumerate(arr):
        if target_sum - num in numbers:
            return [numbers[target_sum - num], index]
        else:
            numbers[arr[index]] = index
    return [-1, -1] # no result found


def remove_duplicates(arr):
    if len(arr) <= 1:
        return -1
    next_unique_value = 1
    index = 0
    while index < len(arr):
        if arr[next_unique_value-1] != arr[index]:
            arr[next_unique_value-1] = arr[index]
            next_unique_value += 1
        index += 1
    return next_unique_value