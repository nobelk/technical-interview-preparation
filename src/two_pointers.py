# Problem: Given an array of sorted numbers and a target sum,
# find a pair in the array whose sum is equal to the given target

def find_pair_with_target_sum(arr, target_sum):
    numbers = {}  # store numbers and indices
    for index, num in enumerate(arr):
        if target_sum - num in numbers:
            return [numbers[target_sum - num], index]
        else:
            numbers[arr[index]] = index
    return [-1, -1]  # no result found


# Given an array of sorted numbers, remove all duplicate number instances from it in-place, such that each element appears only once. The relative order of the elements should be kept the same and you should not use any extra space so that that the solution have a space complexity of O(1).
def remove_duplicates(arr):
    if len(arr) <= 1:
        return -1
    next_unique_value = 1
    index = 0
    while index < len(arr):
        if arr[next_unique_value - 1] != arr[index]:
            arr[next_unique_value - 1] = arr[index]
            next_unique_value += 1
        index += 1
    return next_unique_value


# Given a sorted array, create a new array containing squares of all the numbers of the input array in the sorted order.
def square_sorted_array(arr):
    if len(arr) < 2:
        return [arr[0] * arr[0]]

    rList = [0 for index in range(len(arr))]
    leftIndex = 0
    rightIndex = len(arr) - 1
    highestIndex = len(arr) - 1

    while leftIndex <= rightIndex:
        if arr[leftIndex] * arr[leftIndex] > arr[rightIndex] * arr[rightIndex]:
            rList[highestIndex] = arr[leftIndex] * arr[leftIndex]
            leftIndex += 1
        else:
            rList[highestIndex] = arr[rightIndex] * arr[rightIndex]
            rightIndex -= 1
        highestIndex -= 1

    return rList
