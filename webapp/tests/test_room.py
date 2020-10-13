import pytest
from microbit_app.db import get_db


def test_index(client, auth):
    response = client.get('/')
    assert b"Log In" in response.data
    assert b"History" in response.data
    assert b'User' not in response.data
    assert b"Edit" not in response.data
    assert b"gozip" in response.data
    assert b"5.0x6.0m" in response.data
    assert b"Not active" in response.data

    auth.login()
    response = client.get('/')
    assert b'Log Out' in response.data
    assert b'User' in response.data
    assert b'Edit' in response.data
    assert b'New room' in response.data

@pytest.mark.parametrize('path', (
    '/microbit/gozip',
    '/room/1',
    '/auth/users',
))
def test_login_required(client, path):
    response = client.post(path)
    assert response.headers['Location'] == 'http://localhost/auth/login'

@pytest.mark.parametrize('path', (
    '/4',
    '/microbit/nozip',
))
def test_exists_required(client, auth, path):
    auth.login()
    assert client.post(path).status_code == 404

def test_create(client, auth, app):
    with app.app_context():
        db = get_db()
        precount = db.execute('SELECT COUNT(id) FROM room').fetchone()[0]

    auth.login()
    assert client.get('/room/new').status_code == 200
    client.post('/room/new', data={'description': 'created', 'width': '1', 'deepth': '1'})

    with app.app_context():
        db = get_db()
        count = db.execute('SELECT COUNT(id) FROM room').fetchone()[0]
        assert (precount + 1) == count


def test_update(client, auth, app):
    auth.login()
    assert client.get('/room/2').status_code == 200
    client.post('/room/2', data={'description': 'updated', 'width': '5', 'deepth': '6'})

    with app.app_context():
        db = get_db()
        post = db.execute('SELECT * FROM room WHERE id = 3').fetchone()
        assert post['description'] == 'updated'
        assert post['width'] == '5'
        assert post['deepth'] == '6'


@pytest.mark.parametrize('path', (
    '/room/new',
    '/room/1',
))
def test_create_update_validate(client, auth, path):
    auth.login()
    response = client.post(path, data={'description': ''})
    assert b'Room needs a description' in response.data

def test_delete(client, auth, app):
    auth.login()
    response = client.post('/3/delete')
    assert response.headers['Location'] == 'http://localhost/'

    with app.app_context():
        db = get_db()
        post = db.execute('SELECT * FROM room WHERE id = 3').fetchone()
        assert post is None