from array_shift import insert_shift_array
import pytest

array_one = [1, 2, 3, 5, 6]
array_two = [7, 8, 9, 11, 12, 13]

#odd list
def test_one():       
  expected = [1, 2, 3, 4, 5, 6]
  actual = insert_shift_array(array_one, 4)
  assert actual == expected

#even list
def test_two():       
  expected = [7, 8, 9, 10, 11, 12, 13]
  actual = insert_shift_array(array_two, 10)
  assert actual == expected

def test_three():
  with pytest.raises(TypeError):  # Pass in the expected error
    insert_shift_array('String', 'x')
