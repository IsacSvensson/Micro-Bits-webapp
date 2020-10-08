import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from webapp.microbit_app.db import get_db
from webapp.microbit_app.auth import login_required

bp = Blueprint('microbit', __name__, url_prefix='/microbit')

@bp.route('/<string:id>', methods=('GET', 'POST'))
@login_required
def configMicroBit(id):
    db = get_db()
    if request.method == 'POST':
        name = request.form['description']
        x = request.form['xpos']
        y = request.form['ypos']
        minTemp = request.form['min-temp']
        maxTemp = request.form['max-temp']
        minLight = request.form['min-light']
        maxLight = request.form['max-light']
        mail = request.form['email']
        db.execute('''UPDATE microbit 
                    SET 
                        name = ?, 
                        position_x = ?, 
                        position_y = ?, 
                        min_temp = ?,
                        max_temp = ?,
                        min_light = ?,
                        max_light = ?,
                        mail = ?
                    WHERE id = ?''', (name, x, y, minTemp, maxTemp, minLight, maxLight, mail, id,))
        db.commit()

    thisMb = db.execute("SELECT * FROM microbit WHERE id = ?;", (id, )).fetchone()
    rooms = db.execute("SELECT * FROM room;").fetchall()
    microbits = get_db().execute('SELECT * FROM microbit;').fetchall()
    return render_template('microbit/config.html', microbits = microbits, thisMb=thisMb, rooms = rooms)

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
    db.execute("UPDATE microbit SET room = 'NULL' WHERE id = ?;", (id, ))
    db.commit()

    thisRoom = db.execute("SELECT * FROM room WHERE id = ?;", (oldRoom['room'], )).fetchone()
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
    rooms = db.execute("SELECT * FROM room;").fetchall()
    microbits = get_db().execute('SELECT * FROM microbit;').fetchall()
    return render_template('room/config.html', microbits = microbits, thisRoom=thisRoom, rooms = rooms)
