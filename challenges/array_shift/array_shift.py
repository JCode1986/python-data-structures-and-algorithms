def insert_shift_array(arr, val):
  center = (len(arr)+ 1) // 2
  return arr[:center] + [val] + arr[center:]


#stretch goal- remove middle element
def remove_center(arr):
  center = len(arr) // 2
  return arr[:center] + arr[center + 1:]
