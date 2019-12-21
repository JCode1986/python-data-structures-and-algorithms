from fifo_animal_shelter import AnimalShelter
from stacks_and_queues import Queue
import pytest

@pytest.fixture
def shelter():
    return AnimalShelter()

def test_enqueue_cat_to_cat_q(shelter):
    shelter.fifo_enqueue({'type': 'cat', 'name': 'Garfield'})
    actual = shelter.cat.peek()
    expected = {'type': 'cat', 'name': 'Garfield'}
    assert expected == actual

def test_enqueue_dog_to_dog_q(shelter):
    shelter.fifo_enqueue({'type': 'dog', 'name': 'Pluto'})
    actual = shelter.dog.peek()
    expected = {'type': 'dog', 'name': 'Pluto'}
    assert expected == actual

def test_dequeue_cat_from_cat_q(shelter):
    shelter.fifo_enqueue({'type': 'cat', 'name': 'Felix'})
    actual = shelter.fifo_dequeue('cat')
    expected = {'type': 'cat', 'name': 'Felix'}
    assert expected == actual

def test_dequeue_dog_from_dog_q(shelter):
    shelter.fifo_enqueue({'type': 'dog', 'name': 'Toto'})
    actual = shelter.fifo_dequeue('dog')
    expected = {'type': 'dog', 'name': 'Toto'}
    assert expected == actual
