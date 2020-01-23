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

def test_instantiate_empty_tree(hashmap_one, hashmap_two):
    """Succesfully returns appended value from hashmap two to hashmap one"""
    actual = left_join(hashmap_one, hashmap_two)
    expected = [[['wrath', 'anger', 'delight']], None, [['fond', 'enamored', 'averse'], ['diligent', 'employed', 'idle']], [['outift', 'garb', 'None']], [['guide', 'usher', 'follow']]]
    assert actual == expected
