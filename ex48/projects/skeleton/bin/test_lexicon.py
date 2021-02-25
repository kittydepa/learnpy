from projects.skeleton.bin.ex48 import Numbers
import pytest

from ex48 import UserInput
from ex48 import Numbers

def test_directions():
    lexicon = ['hi there']
    assert lexicon.scan("north") == [('direction', 'north')]
    result = lexicon.scan("north south east")
    assert result == [('direction', 'north'),
                      ('direction', 'south'),
                      ('direction', 'east')]