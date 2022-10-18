def binarySearch(arr, target, low, high):
    while low <= high:
        mid = low + (high-low) //2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid -1
        elif arr[mid] < target:
            low = mid + 1
    return -1
        

