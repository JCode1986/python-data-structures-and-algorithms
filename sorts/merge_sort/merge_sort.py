def merge_sort(arr):

    n = len(arr)

    if n > 1:

        mid = len(n) // 2
        left = n[:mid]
        right = n[mid:]

    merge_sort(left)
    merge_sort(right)

    return merge(merge_sort(left), merge(mergesort_right))

def merge(left, right):

    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    result + left[:i] + right[:j]

    return result

test = [2, 1, 3, 6, 22, 10, 13, 44, 21]
print(merge_sort(test))