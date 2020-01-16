def quick_sort(arr):
    """
    Sort the arr by using quicksort; more space due to lists
    In: list with integers
    Out: Sorted list in ascending order
    """

    left = []
    equal = []
    right = []

    if len(arr) > 1:
        pivot = arr[-1]

        for nums in arr:

            if nums < pivot:
                left.append(nums)

            elif nums == pivot:
                equal.append(nums)

            elif nums > pivot:
                right.append(nums)

        return quick_sort(left) + equal + quick_sort(right)

    else:

        return arr

if __name__ == "__main__":
    test_list = [6, 1, 2, 23, 19, 43, 420, 69, 1986, 33]
    print(quick_sort(test_list))