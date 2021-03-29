import pytest

def test_file1_method1():
    x = 5
    y = 6
    assert x + 2 == y, "test failed because x = " + str(x) + " y = " + str(y) # This prints some more info about the failure IF we get a failure. PyTest also gives some good details on its own though?
    assert x == y, "test failed"

def test_file1_method2():
    x = 5
    y = 6
    assert x + 1 == y, "test failed"
