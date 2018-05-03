"""Parse malformed csv from Uright proprietary app.
# TODO: improve documentation
"""
import chardet
import csv
from datetime import datetime as dt

filetoread = '20180421-all.csv'


def getencoding(filename):
    """Find the encoding of a given file.
    Args:
        filename(string)    file name or complete path
    Returns:
        a string with the format detected, i.e. 'UTF-8' 'ASCII'
    """

    rawdata = open(filename, 'rb').read()
    encoding = chardet.detect(rawdata)['encoding']
    return encoding


class myIterator(object):
    """Attempt to write an iteratorself."""

    def __init__(self, filename):
        """Check file encoding on init."""

        self.f = filename
        self.enc = getencoding(self.f)
        self.badcsv = open(self.f, 'r', encoding=self.enc)

    def __iter__(self):
        return self

    def next(self):
        row = csv.reader(self.badcsv, delimiter="\t")
        self = next(row)


print(getencoding(filetoread))


x = myIterator(filetoread)
print(x.f)
print(x.badcsv)
