# This is binarySearch algorithm
# using mid and dividing array into halves
def binarySearch(arr, first, last, ele):
    while first < last:
        mid = (first + last) // 2
        if arr[mid] == ele:
            return mid
        elif arr[mid] < ele:
            first = mid + 1
        else:
            last = mid

    return "Not found"


# BinarySearch algorithm using Python's
# built-in bisect module
# no need to calculate mid and check again and again
def bSearch(arr, ele):

    from bisect import bisect_left

    pos = bisect_left(arr, ele)

    if pos == len(arr):
        return "Not found"
    else:
        return pos


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    ele = 5

    print(binarySearch(arr, 0, len(arr), ele))

    print(bSearch(arr, ele))