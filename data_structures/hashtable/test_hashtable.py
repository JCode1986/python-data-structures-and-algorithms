from hashtable import HashMap
import pytest

@pytest.fixture
def hash_map():
    return HashMap(10)

@pytest.fixture
def collision_test():
    return HashMap(1)


def test_add_method(hash_map):
    actual = hash_map.add('hello', 33)
    expected = hash_map.contains('hello')
    assert actual == expected

def test_get_method_returns_value(hash_map):
    hash_map.add('hello', 33)
    actual = hash_map.get('hello')
    expected = 33
    assert actual == expected

def test_get_method_returns_none_if_key_does_not_exist(hash_map):
    hash_map.add('hello', 33)
    actual = hash_map.get('hello world')
    expected = None
    assert actual == expected

def test_successfully_hash_key(hash_map):
    actual = hash_map.hash('hash me up')
    expected = 7
    assert actual == expected

def test_handles_collision_and_returns_correct_value(collision_test):
    collision_test.add('one', 420)
    collision_test.add('is', 1986)
    collision_test.add('a', 23)
    collision_test.add('collision', 69)
    actual = [collision_test.get('collision'), collision_test.get('one')]
    assert actual == [69, 420]
