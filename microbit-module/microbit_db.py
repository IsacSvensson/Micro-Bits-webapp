import sqlite3
from datetime import date

def get_db():
    """
    Returns a sqlite3-object.
    """
    db = sqlite3.connect("./../webapp/instance/microbit_app.sqlite")
    return db

def dbInsert(what, obj):
    """
    Input: (string) what: string that tells function what to insert,
    MicroBit-object\n
    Inserts new MicroBit- or history-entry, depending on input.
    """
    db = get_db()
    
    with db as c:
        if what == "microbit":
            if len(obj.devName) != 5:
                print('Error: Corrupted data')
                return False 
            c.execute("INSERT INTO microbit (id, status) VALUES (?, 'Active');", (obj.devName,))
        elif what == "history":
            if obj.readValues():
                c.execute("""
                INSERT INTO history 
                    (microbit, min_temp, max_temp, min_light, max_light)
                VALUES 
                    (?,?,?,?,?);
                """, (obj.devName, obj.temp, obj.temp, obj.light, obj.light))
                c.execute("UPDATE microbit SET status = 'Active' WHERE id = ?;", (obj.devName,))
            else:
                c.execute("INSERT INTO history (microbit) VALUES (?);", obj.devName)
                c.execute("UPDATE microbit SET status = 'Not active' WHERE id = ?;", (obj.devName,))
    db.commit()

def dbUpdate(obj, date, what = None):
    """
    
    """
    db = get_db()
    
    with db as c:
        if what == 'microbit':
            c.execute("UPDATE microbit SET temp = ?, light = ? WHERE id = ?;", (obj.temp, obj.light, obj.devName,))
        sql = ("UPDATE history " + 
            "SET min_temp = ?, max_temp = ?, min_light = ?, max_light = ? "+
            "WHERE microbit = ? AND date = ?;")
        c.execute(sql, (obj.minTemp, obj.maxTemp, obj.minLight, obj.maxLight, obj.devName, date,))
        c.execute("UPDATE microbit SET status = 'Active' WHERE id = ?;", (obj.devName,))

    db.commit()

def dbSetStatus(obj, status):
    db = get_db()
    
    with db as c:
        sql = ("UPDATE microbit " + 
            "SET status = ? "+
            "WHERE id = ?;")
        c.execute(sql, (status, obj.devName,))
    db.commit()
    print("{} is {}".format(obj.devName, status))

def getMicroBits():
    db = get_db()
    with db as c:
        toReturn = c.execute("SELECT id FROM microbit;").fetchall()
    return toReturn

def getHistory():
    thisDate = date.today().strftime("%Y-%m-%d")
    db = get_db()
    with db as c:
        toReturn = c.execute("SELECT * FROM history where date = ?;", (thisDate,)).fetchall()
    return toReturn