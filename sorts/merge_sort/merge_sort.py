def merge_sort(arr): 
    n = len(arr)

    if n == 0 or n == 1: 
        return arr

    mid = n // 2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)
    merge(left, right, arr)
    
    return arr


def merge(left, right, arr):

    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
    
        k += 1

    if i == len(left): 
        while j < len(right): 
            arr[k] = right[j]
            j += 1
            k += 1

    else: 
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1


test = [2, 1, 3, 6, 22, 10, 13, 44, 21]
print(merge_sort(test))


# was attempting a different approach

# def merge_sort(arr):

#     n = len(arr)

#     if n > 1:
#         mid = n // 2
#         left = arr[:mid]
#         right = arr[mid:]

#         merge_sort(left)
#         merge_sort(right)

#         return merge(merge_sort(left), merge_sort(right))

# def merge(left, right):

#     result = []
#     i = 0
#     j = 0

#     while i < len(left) and j < len(right):

#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1

#         else:
#             result.append(right[j])
#             j += 1

#     result + left[:i] + right[:j]

#     return result