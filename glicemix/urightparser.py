#!/usr/bin/env python
''' urightparser.py
load malformed csv exported from uright app and parse with
regex
'''
import re


def parse(filename):
    try:
        open(filename, 'r', encoding='UTF-16')
    except FileNotFoundError:
        print('File non trovato')
        return None
    with open(filename, 'r', encoding='UTF-16') as badcsv:
        next(badcsv)        # Skip first line that has column names
        for row in badcsv:
            mdate = re.findall(r'\d{2}/\d{2}/\d{4}', row)
            mtime = re.findall(r'\d{2}\.\d{2}', row)
            mvalue = re.findall(r'Glucose\s="(\d{1,3})\s', row)
            mtype = re.findall(r'"(AC|Gen|PC)"', row)
            measurement = *mdate, *mtime, *mvalue, *mtype
            print(measurement)
