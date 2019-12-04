from array_binary_search import binary_search

array_one = [2, 4, 6, 8, 10, 11, 13, 15, 16, 21, 30, 32, 45, 60]

#returns index of value if present
def test_one():
  expected = 9
  actual = binary_search(array_one, 21)
  assert actual == expected

def test_two():
  expected = 4
  actual = binary_search(array_one, 10)
  assert actual == expected

#not in list
def test_three():
  expected = -1
  actual = binary_search(array_one, 12)
  assert actual == expected
