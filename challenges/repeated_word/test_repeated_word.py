from repeated_word import first_repeated_word, most_repeated_word
import pytest

def test_returns_first_repeated_word():
    sentence = 'In a galaxy far far away'
    actual = first_repeated_word(sentence)
    expected = 'far'
    assert actual == expected

def test_more_than_one_repeated_word_in_string():
    sentence = 'The word the is the first repeated word in this sentence. Testing: 1 1 1 1 1 1'
    actual = first_repeated_word(sentence)
    expected = 'the'
    assert actual == expected

def test_lower_or_uppercase_does_not_matter():
    sentence = 'It does not matter. -- it --'
    actual = first_repeated_word(sentence)
    expected = 'it'
    assert actual == expected

def test_string_with_punctuations():
    sentence_with_punctuations = 'In a galaxy far, far, far... away. Boo boo'   
    actual = first_repeated_word(sentence_with_punctuations)
    expected = 'far'
    assert actual == expected

def test_returns_most_repeated_word():
    sentence = 'In a galaxy far far away. In a galaxy even further away. Hey hey hey hey hey.'  
    actual = most_repeated_word(sentence)
    expected = 'hey'
    assert actual == expected   

