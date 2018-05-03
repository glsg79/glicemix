"""This is a the database module."""

import sqlite3
import csv
from datetime import datetime as dt


def connection(dbf):
    '''Create connection with the database
    param:  dbf  database file name
    return: connection object or None
    '''
    conn = None
    try:
        conn = sqlite3.connect('test.db')
        return conn
    except sqlite3.Error as e:
        print(e)
    return None


def tblcreate(conn):
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS tblSugarLevels (
    mDate text(10),
    mTime text(5),
    mLevel integer,
    mType text(1),
    PRIMARY KEY (mDate, mTime)
    ) WITHOUT ROWID;''')


""" # TODO: Creare del codice per fare un check del database
def checkdb():
    cur.execute('''PRAGMA table_info(tblSugarLevels);''')
    print(cur.fetchall())
"""


def importfromfile(f):
    ''' Insert all data coming from a malformed csv file from the manufacturer
    application of my glucose meter in the sqlite database row by row

    param:  f   name of the text file to load

    # TODO: less hardcoded variables like database name etc
    # TODO: code cleanup
    # TODO: check for duplicate, conflict and wrong data (due to export malfunctioning)
    '''
    clean_input = str.maketrans('.', ':', ' ="')
    mtypedict = {'Gen': 'X', 'AC': 'P', 'PC': 'D'}
    stmt = '''INSERT INTO tblSugarLevels(mDate, mTime , mLevel, mType)
              VALUES(?,?,?,?)'''
    conn = connection('test.db')

    with open(f, 'r', encoding='utf-16') as badcsv:
        rows = csv.reader(badcsv, delimiter="\t")
        next(rows, None)  # Skip first line that has column names

        for row in rows:
            mdate = row[2].translate(clean_input)
            mdate = dt.strftime(dt.strptime(mdate, '%d/%m/%Y'), '%Y-%m-%d')
            mtime = row[3].translate(clean_input)
            mlevel = row[5][:-6].translate(clean_input)
            mtype = mtypedict[row[7].translate(clean_input)]

            # measurement = [mdate, mtime, mlevel, mtype]
            # print(measurement)
            cur = conn.cursor()
            cur.execute(stmt, (mdate, mtime, mlevel, mtype))
        conn.commit()


def eliminatabella(conn):
    cur = conn.cursor()
    cur.execute('''DROP TABLE IF EXISTS tblSugarLevels''')


# conn = connection('test.db')
# tblcreate(conn)
# eliminatabella(conn)

# checkdb()
# importfromfile('20180421-all.csv')
