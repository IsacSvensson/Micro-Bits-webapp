import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.exceptions import abort
from microbit_app.db import get_db
from microbit_app.auth import login_required

bp = Blueprint('room', __name__, url_prefix='/room')

@bp.route('/<int:id>', methods=('GET', 'POST'))
@login_required
def configRoom(id):
    db = get_db()
    if request.method == 'POST':
        print(id)
        roomId = id
        description = request.form['description']
        width = request.form['width']
        deepth = request.form['deepth']
        db.execute("UPDATE room SET description = ?, width = ?, deepth = ? WHERE id = ?;", (description, width,deepth,roomId,))
        db.commit()

    thisRoom = db.execute("SELECT * FROM room WHERE id = ?;", (id, )).fetchone()
    if not thisRoom:
        abort(404, description="404 - Room not found")

    rooms = db.execute("SELECT * FROM room;").fetchall()
    microbits = get_db().execute('SELECT * FROM microbit;').fetchall()
    return render_template('room/config.html', microbits = microbits, thisRoom=thisRoom, rooms = rooms)

@bp.route('/<int:id>/delete', methods=('GET', 'POST'))
@login_required
def deleteRoom(id):
    db = get_db()
    db.execute("DELETE FROM room WHERE id = ?;", (id, ))
    db.commit()
    return redirect(url_for('monitor.index'))

@bp.route('<string:id>/deletemicrobit', methods=('GET', 'POST'))
@login_required
def deleteMicroBit(id):
    db = get_db()
    oldRoom = db.execute("SELECT room FROM microbit WHERE id = ?;", (id, )).fetchone()
    if not oldRoom:
        abort(404, description="404 - Room not found")

    db.execute("UPDATE microbit SET room = 'NULL' WHERE id = ?;", (id, ))
    db.commit()

    thisRoom = db.execute("SELECT * FROM room WHERE id = ?;", (oldRoom['room'], )).fetchone()
    if not thisRoom:
        abort(404, description="404 - Room not found")

    rooms = db.execute("SELECT * FROM room;").fetchall()
    microbits = get_db().execute('SELECT * FROM microbit;').fetchall()
    return render_template('room/config.html', microbits = microbits, thisRoom=thisRoom, rooms = rooms)

@bp.route('<int:id>/addmicrobit', methods=('GET', 'POST'))
@login_required
def addMicroBit(id):
    db = get_db()
    microbit = request.form.get('microbit')
    db.execute("UPDATE microbit SET room = ? WHERE id = ?", (id, microbit,))
    db.commit()

    thisRoom = db.execute("SELECT * FROM room WHERE id = ?;", (id, )).fetchone()
    if not thisRoom:
        abort(404, description="404 - Room not found")

    rooms = db.execute("SELECT * FROM room;").fetchall()
    microbits = get_db().execute('SELECT * FROM microbit;').fetchall()
    return render_template('room/config.html', microbits = microbits, thisRoom=thisRoom, rooms = rooms)

@bp.route('/new', methods=('GET', 'POST'))
@login_required
def newRoom():
    db = get_db()
    if request.method == 'POST':
        error = None
        description = request.form['description']
        if description is None:
            error = "Room needs a description"
        elif description in db.execute('SELECT description FROM room;').fetchall():
            error = "Description is used for another room"
        else:
            width = request.form['width']
            deepth = request.form['deepth']
            db.execute("INSERT INTO room (description, width, deepth) VALUES (?,?,?);", (description,width,deepth,))
            db.commit()

            newroom = db.execute('SELECT id FROM room WHERE description = ?;', (description,)).fetchone()
            return redirect(url_for('monitor.room', id=newroom['id']))
        flash(error)
    rooms = db.execute("SELECT * FROM room;").fetchall()
    return render_template('room/new.html', rooms=rooms)