
# What as given by the author. Now, write the code that will make this GO

# from projects.skeleton.bin.ex48 import Scanner
import pytest

from ex48_attempt2 import scan
from ex48_attempt2 import convert_number
from ex48_attempt2 import lexicon


def test_directions():
    assert scan("north") == [('direction', 'north')] # Ensure that when north is called within Scan, this is the output
    result = scan("north south east") # ensure that, this result of input with san, will result in NEXT LINE
    assert result == [('direction', 'north'), # That it will be like this
                      ('direction', 'south'),
                      ('direction', 'east')]


def test_verbs():

    assert scan("go") == [('verb', 'go')]
    result = scan("go kill eat")
    assert result == [('verb', 'go'),
                      ('verb', 'kill'),
                      ('verb', 'eat')]


def test_stops():

    assert scan("the") == [('stop', 'the')]
    result = scan("the in of")
    assert result == [('stop', 'the'),
                      ('stop', 'in'),
                      ('stop', 'of')]


def test_nouns():

    assert scan("bear") == [('noun', 'bear')]
    result = scan("bear princess")
    assert result == [('noun', 'bear'),
                      ('noun', 'princess')]


def test_numbers():

    assert scan("1234") == [('number', 1234)]
    result = scan("3 91234")
    assert result == [('number', 3),
                      ('number', 91234)]


def test_errors():

    assert scan("ASDFADFASDF") == [('error', 'ASDFADFASDF')] # ensure that this will be an error
    result = scan("bear IAS princess") # ensure that this will be an error for IAS, but the rest will not be
    assert result == [('noun', 'bear'),
                      ('error', 'IAS'),
                      ('noun', 'princess')]
