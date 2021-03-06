import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.exceptions import abort
from microbit_app.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        
        return view(**kwargs)
    return wrapped_view

@bp.route('/register', methods=('GET', 'POST'))
@login_required
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db =get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error =  'Password is required.'
        elif db.execute(
            'SELECT id FROM user WHERE username = ?', (username,)
        ).fetchone() is not None:
            error = 'User {} is already registered.'.format(username)
        
        if error is None:
            db.execute('INSERT INTO user (username, password) VALUES (?, ?)', 
                (username, generate_password_hash(password))
            )
            db.commit()
            return redirect(url_for('auth.users'))
        flash(error)
    
    return render_template('auth/register.html')

@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    db = get_db()
    error = None
    if request.method == 'POST':
        if not (db.execute("SELECT id FROM user WHERE id = ?;", (id,)).fetchone()):
            error = "No user with this id"
        elif (len(db.execute("SELECT id FROM user;").fetchall()) <= 1):
            error = "You can not remove the last user"
        else:
            db.execute('DELETE FROM user WHERE id = ?', (id,))
            db.commit()
            return redirect(url_for('auth.users'))
        flash(error)
    users = db.execute("SELECT id, username FROM user;").fetchall()
    return render_template('auth/users.html', users=users)

@bp.route('/<int:id>/edit', methods=('GET', 'POST'))
@login_required
def edit(id):
    db =get_db()
    user = db.execute("SELECT id, username FROM user WHERE id = ?;", (id, )).fetchone()
    if not user:
        abort(404, description="404 - User not found")

    if request.method == 'POST':
        password = request.form['password']
        error = None

        if not password:
            error =  'Password is required.'
        
        if error is None:
            db.execute('UPDATE user set password = ? WHERE id = ?', 
                (generate_password_hash(password), id,)
            )
            db.commit()
            return redirect(url_for('auth.users'))
        flash(error)
    
    return render_template('auth/edit.html', user=user)

@bp.route('/users')
@login_required
def users():
    db = get_db()

    users = db.execute("SELECT id, username FROM user;").fetchall()
    return render_template('auth/users.html', users=users)

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))
        flash(error)

    return render_template('auth/login.html')

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id, )
        ).fetchone()

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

