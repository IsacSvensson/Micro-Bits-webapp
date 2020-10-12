from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from microbit_app.auth import login_required
from microbit_app.db import get_db

bp = Blueprint('monitor', __name__)

colors = [
    '#000000',
    '#FF0000',
    '#008000',
    '#0000FF',
    '#FF00FF'
]

@bp.route('/')
def index():
    db = get_db()
    microbits = db.execute('SELECT * FROM microbit;').fetchall()
    rooms = db.execute('SELECT * FROM room;').fetchall()
    print()
    return render_template('monitor/index.html', microbits=microbits, rooms=rooms, colors=colors)

@bp.route('/<int:id>')
def room(id):
    room = get_db().execute('SELECT * FROM room WHERE id=?;', (id,)).fetchall()
    rooms = get_db().execute('SELECT * FROM room;').fetchall()
    microbits = get_db().execute('SELECT * FROM microbit;').fetchall()

    return render_template('monitor/room.html', thisRoom = room, rooms = rooms, microbits = microbits, colors=colors)

@bp.route('/history')
def history():
    db = get_db()
    history = db.execute("SELECT * FROM history ORDER BY date DESC;")
    return render_template('monitor/history.html', history=history)