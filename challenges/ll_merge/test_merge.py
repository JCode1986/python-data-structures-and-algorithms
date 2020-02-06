from ll_merge import merge_lists, Node, Linked_list
import pytest

@pytest.fixture
def list1():
    list1 = Linked_list()
    list1.insert(1)
    array = [3, 5, 7, 9]
    for num in array:
        list1.append(num)
    return list1

@pytest.fixture
def list2():
    list2 = Linked_list()
    list2.insert(2)
    list2.append(4)
    list2.append(6)
    list2.append(8)
    list2.append(10)
    return list2

# def test_merge_lists(list1, list2):
#     actual = merge_lists(list1, list2)
#     expected = 0
#     assert actual == expected 

print(list1)