def insertion_sort(lst):
  """
  Sorts list from lowest to highest using insertion sort method
  In - takes in a list of integers
  Out - returns a list of sorted integers  
  """

  for i in range(1, len(lst)):
    j = i - 1
    temp = int((lst[i]))

    while j >= 0 and temp < lst[j]:
      lst[j + 1] = lst[j]
      j = j - 1
    lst[j + 1] = temp

  return lst

test_lst = [18,22,1,13,53,64] 
print(insertion_sort(test_lst))
