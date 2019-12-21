from ll_merge import merge_lists, Node, Linked_list
import pytest

@pytest.fixture
def list1():
    list1 = Linked_list()
    l1st1.insert(1)
    array = [3, 5, 7, 9]
    for num in array:
        list1.append(num)
    # l1st1.append(3)
    # l1st1.append(5)
    # l1st1.append(7)
    # l1st1.append(9)
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

def test_merge_lists(list1, list2):
    actual = merge_lists(list1, list2)
    expected = 0
    assert actual == expected 