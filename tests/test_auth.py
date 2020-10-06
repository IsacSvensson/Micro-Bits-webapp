import pytest
from flask import g, session
from webapp.microbit_app.db import get_db

def test_login(client, auth):
    assert client.get('/auth/login').status_code == 200
    response = auth.login()
    assert response.headers['Location'] == 'http://localhost/'

    with client:
        client.get('/')
        assert session['user_id'] == 2
        assert g.user['username'] == 'test'


@pytest.mark.parametrize(('username', 'password', 'message'), (
    ('a', 'test', b'Incorrect username.'),
    ('test', 'a', b'Incorrect password.'),
))
def test_login_validate_input(auth, username, password, message):
    response = auth.login(username, password)
    assert message in response.data

def test_logout(client, auth):
    auth.login()

    with client:
        auth.logout()
        assert 'user_id' not in session

def test_register(client, app, auth):
    auth.login()
    assert client.get('/auth/register').status_code == 200
    response = client.post(
        '/auth/register', data={'username': 'a', 'password': 'a'}
    )
    assert 'http://localhost/auth/users' == response.headers['Location']

    with app.app_context():
        assert get_db().execute(
            "SELECT * FROM user WHERE username = 'a'",
        ).fetchone() is not None


@pytest.mark.parametrize(('username', 'password', 'message'), (
    ('', '', b'Username is required.'),
    ('a', '', b'Password is required.'),
    ('test', 'test', b'already registered'),
))
def test_register_validate_input(client, username, password, message, auth):
    auth.login()
    response = client.post(
        '/auth/register',
        data={'username': username, 'password': password},
        follow_redirects=True
    )
    print(response.data)
    assert message in response.data

def test_edit_user(client, app, auth):
    auth.login()
    assert client.get('/auth/1/edit').status_code == 200
    response = client.post(
        '/auth/1/edit', data={'password': 'katt'}
    )
    assert 'http://localhost/auth/users' == response.headers['Location']
    auth.logout()

    with client:
        auth.logout()
        assert 'user_id' not in session
        auth.login('admin', 'katt')
        assert session['user_id'] == 1

def test_edit_validate_input(client, app, auth):
    auth.login()
    assert client.get('/auth/1/edit').status_code == 200
    response = client.post(
        '/auth/1/edit', data={'password': ''}
    )
    assert b'Password is required.' in response.data
    auth.logout()

@pytest.mark.parametrize(('id'), (
    ('1'),
    ('3'),
))
def test_delete_user(client, id, app, auth):
    auth.login()
    assert client.get().status_code == 200
    response = client.post(
        '/auth/%s/delete' % (id), follow_redirects=True
    )
    assert 'auth/%s/edit' % (id) not in str(response.data)