"""Parse malformed csv from Uright proprietary app.

# TODO: improve documentation
"""
import chardet
import csv
from datetime import datetime as dt


def getencoding(f):
    """Find the encoding of a given file.

    Args:
        f(string)    file name or complete path
    Returns:
        a string with the format detected, i.e. 'UTF-8' 'ASCII'
    """
    rawdata = open(f, 'rb').read()
    encoding = chardet.detect(rawdata)['encoding']
    return encoding


def urightparse(f, enc=None):
    """Parse the file exported by the Uright windows applicationself.

    Args:
        f(string)   the file name to parse
        enc(string) the file encoding if known else it is detected by chardet
    Returns:
        a list of tuples or dictionaries with all I need
    """
    if enc == None:
        enc = getencoding(f)

    clean_input = str.maketrans('.', ':', ' ="')
    mtypedict = {'Gen': 'X', 'AC': 'B', 'PC': 'A'}
    measurement = []

    with open(f, 'r', encoding=enc) as badcsv:
        rows = csv.reader(badcsv, delimiter="\t")
        next(rows, None)  # Skip first line that has column names

        for row in rows:
            m_date = row[2].translate(clean_input)
            m_date = dt.strftime(dt.strptime(m_date, '%d/%m/%Y'), '%Y-%m-%d')
            m_time = row[3].translate(clean_input)
            m_level = row[5][:-6].translate(clean_input)
            m_type = mtypedict[row[7].translate(clean_input)]

            measurement.append((m_date, m_time, m_level, m_type))
    return measurement


# Testing
# filetoread = '/home/glsg/Projects/glicemix/20180421-all.csv'
# enc = getencoding(filetoread)
# result = urightparse(filetoread, enc)

# print(result)
