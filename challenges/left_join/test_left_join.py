from left_join import HashMap, left_join
import pytest

@pytest.fixture
def hashmap_one():
    h1 = HashMap(5)
    h1.add('fond', 'enamored')
    h1.add('wrath', 'anger')
    h1.add('diligent', 'employed')
    h1.add('outift', 'garb')
    h1.add('guide', 'usher')    
    return h1

@pytest.fixture
def hashmap_two():
    h2 = HashMap(5)
    h2.add('fond', 'averse')
    h2.add('wrath', 'delight')
    h2.add('diligent', 'idle')
    h2.add('guide', 'follow')
    h2.add('flow', 'jam') 
    return h2

def test_returns_values_if_both_keys_are_present():
    h1 = HashMap(1)
    h2 = HashMap(1)
    h1.add('wrath', 'anger')
    h2.add('wrath', 'delight')
    expected = [[['wrath', 'anger', 'delight']]]
    actual = left_join(h1, h2)
    assert actual == expected

def test_returns_None_in_bucket_if_key_is_not_preset():
    h1 = HashMap(1)
    h2 = HashMap(1)
    h1.add('wrath', 'anger')
    h2.add('flow', 'jam')
    expected = [[['wrath', 'anger', None]]]
    actual = left_join(h1, h2)
    assert actual == expected

def test_returns_map_of_both_hashmaps_in_one_data_structure(hashmap_one, hashmap_two):
    """Succesfully returns appended value from hashmap two to hashmap one"""
    actual = left_join(hashmap_one, hashmap_two)
    expected = [[['wrath', 'anger', 'delight']], None, [['fond', 'enamored', 'averse'], ['diligent', 'employed', 'idle']], [['outift', 'garb', None]], [['guide', 'usher', 'follow']]]
    assert actual == expected
