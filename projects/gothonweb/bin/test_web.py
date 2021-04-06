import pytest
from web import app

app.config['TESTING'] = True
webz = app.test_client()

def test_index():
    rv = webz.get('/', follow_redirects = True)
    assert rv.status_code == 404

    rv = webz.get('/hello', follow_redirects = True)
    assert rv.status_code == 200
    assert b"Fill Out This Form" in rv.data # Need b because bytes yo, not str

    data = {'name': 'Kitty', 'greet': 'Hej'}
    rv = webz.post('/hello', follow_redirects = True, data = data)
    assert b"Kitty" in rv.data
    assert b"Hej" in rv.data
