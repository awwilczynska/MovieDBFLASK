import sqlite3

def get_db():
    db = sqlite3.connect('movies.db', check_same_thread=False)
    return db

def listMovies():
    db = get_db()
    try:
        cursor = db.cursor()
        cursor.execute('SELECT * FROM movies')
        results = cursor.fetchall()
        return results
    finally:
        db.close()

def addMovie(title, year, actors):
    db = get_db()
    try:
        cursor = db.cursor()
        cursor.execute('INSERT INTO movies (title, year, actors) VALUES (?, ?, ?)', (title, year, actors))
        db.commit()
    finally:
        db.close()

def removeMovie(ids):
    db = get_db()
    try:
        cursor = db.cursor()
        cursor.executemany('DELETE FROM movies WHERE id = ?', [(id,) for id in ids])
        db.commit()
        deletedRows = cursor.rowcount
        return deletedRows
    finally:
        db.close()

def findMovie(key):
    db = get_db()
    try:
        cursor = db.cursor()
        cursor.execute('SELECT * FROM movies WHERE title LIKE ? OR actors LIKE ?', ("%"+key+"%", "%"+key+"%"))
        results = cursor.fetchall()
        return results
    finally:
        db.close()
