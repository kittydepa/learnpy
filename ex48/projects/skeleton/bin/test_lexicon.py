import pytest

from ex48 import lexicon

def test_directions():
    assert lexicon.scan("north") == [('direction', 'north')]
    result = lexicon.scal("north south east")
    assert result == [('direction', 'north'),
                      ('direction', 'south'),
                      ('direction', 'east')]