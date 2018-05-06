"""This is a the database module."""

import sqlite3
from urightparser import urightparse


def getconnection(db_file):
    """Create connection with the database.

    param:  dbf  database file name
    return: connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return None


def createdb(conn):
    cur = conn.cursor()
    with open('glicemix_schema.sql') as schema:
        cur.executescript(schema.read())


""" # TODO: Creare del codice per fare un check del database
def checkdb():
    cur.execute('''PRAGMA table_info(tblSugarLevels);''')
    print(cur.fetchall())
"""


def checkdb(db_file):
    magicheader = '53514C69746520666F726D6174203300'
    app_ID = '0002998B'
    hex_header = ''
    try:
        file_header = open(db_file, 'rb').read(100)
    except FileNotFoundError as fnf:
        print(fnf)

    hex_header = ''.join(['{:02X}'.format(byte) for byte in file_header])

    if (hex_header[:32] == magicheader) and (hex_header[136:144] == app_ID):
        pass
        # print('{}  check ok. :)'.format(db_file))
    else:
        raise BaseException('{} is not a valid database file'.format(db_file))
        # TODO: Implement a FileValidationError exception


def importfromfile(f):
    """Import data coming from the file exported by Uright application.

    param:  f   name of the text file to load

    # FIXME: hardcoded variables like database name etc
    # TODO: check for duplicate, conflict and wrong data (due to export malfunctioning)
    """
    stmt = '''INSERT INTO measurements(m_date, m_time , m_level, m_type)
              VALUES(?,?,?,?)'''

    conn = getconnection('test.db')
    cur = conn.cursor()
    alldata = urightparse(f)

    cur.executemany(stmt, alldata)
    conn.commit()


# ------ PLAYGROUND ------
checkdb('test.db')
# conn = getconnection('test.db')
# createdb(conn)
importfromfile('20180421-all.csv')

# filetoread = '/home/glsg/Projects/glicemix/20180421-all.csv'
# schemata(conn)
# importfromfile(filetoread)
# tblcreate(conn)
# eliminatabella(conn)
