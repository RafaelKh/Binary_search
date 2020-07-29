def binary_search(arr, x):
    arr = sorted(arr)
    l = 0
    e = len(arr) - 1
    while l <= e:
        mid = (e + l) // 2
        if arr[mid] < x:
            l = mid + 1
        elif arr[mid] > x:
            e = mid - 1
        else:
            return mid
    return -1


result = binary_search([2, 14, 84, 45, 3, 21, 4, 10, 40], 5)

if result != -1:
    print('Element exists')
else:
    print("Element doesn't exist")
