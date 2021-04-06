'''
The purpose of this testing script is to test the web app, rather than
manually doing it, refreshing the page and adding the input, etc. 
'''

import pytest
from web import app # whole appe here. 

app.config['TESTING'] = True # Read more here: https://flask.palletsprojects.com/en/1.1.x/config/
webz = app.test_client() # Read more here: https://flask.palletsprojects.com/en/1.1.x/testing/ 

def test_index():
    rv = webz.get('/', follow_redirects = True)
    assert rv.status_code == 404 # Make sure it returns 'Does not Exist' because it does not yet; just the local...w.e URL.

    rv = webz.get('/hello', follow_redirects = True)
    assert rv.status_code == 200 # This one though, /hello, should exist. 
    assert b"Fill Out This Form" in rv.data # Need b because bytes yo, not str

    data = {'name': 'Kitty', 'greet': 'Hej'} # flask API for processing requests; this line and the next
    rv = webz.post('/hello', follow_redirects = True, data = data)
    assert b"Kitty" in rv.data
    assert b"Hej" in rv.data
