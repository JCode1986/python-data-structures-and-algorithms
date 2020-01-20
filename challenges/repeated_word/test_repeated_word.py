from repeated_word import repeated_word
import pytest

def test_returns_first_repeated_word():
    sentence = 'In a galaxy far far away'
    actual = repeated_word(sentence)
    expected = 'far'
    assert actual == expected

def test_more_than_one_repeated_word_in_string():
    sentence = 'The word the is the first repeated word in this sentence. Testing: 1 1 1 1 1 1'
    actual = repeated_word(sentence)
    expected = 'the'
    assert actual == expected