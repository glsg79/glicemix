"""Parse malformed csv from Uright proprietary app.

# TODO: improve documentation
"""
import chardet
import csv
import datetime as dt
import pandas as pd
from pprint import pprint


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


def time_in_range(startstr, endstr, xstr):
	"""Return true if xstr is in the range [startstr, endstr].

	Use the HH:MM string startstr, endstr, and xstr.
	"""
	start = dt.datetime.strptime(startstr, '%H:%M').time()
	end = dt.datetime.strptime(endstr, '%H:%M').time()
	x = dt.datetime.strptime(xstr, '%H:%M').time()

	if start <= end:
		return start <= x <= end
	else:
		return start <= x or x <= end


def set_mtype(when, category):
	"""
	Return a more precise type of measurement.

	TODO: Implementare un sistema di recupero degli orari di inizio e fine
	periodo dalla tabella di configurazione.

	:param when: measurement time string 'HH:MM'
	:param category: raw measurement category (AC, PC, Gen)
	:return: string describing the measurement time
	"""
	bb_min = '04:30'
	bb_max = '11:30'

	bl_min = '11:40'
	bl_max = '14:00'

	bd_min = '18:30'
	bd_max = '21:30'

	ab_min = '06:30'
	ab_max = '12:45'

	al_min = '13:40'
	al_max = '16:00'

	ad_min = '20:30'
	ad_max = '00:30'

	if category == 'Gen':
		return 'Misurazione extra'
	elif category == 'AC':
		if time_in_range(bb_min, bb_max, when):
			return 'Prima di colazione'
		if time_in_range(bl_min, bl_max, when):
			return 'Prima di pranzo'
		if time_in_range(bd_min, bd_max, when):
			return 'Prima di cena'
	elif category == 'PC':
		if time_in_range(ab_min, ab_max, when):
			return 'Dopo colazione'
		if time_in_range(al_min, al_max, when):
			return 'Dopo pranzo'
		if time_in_range(ad_min, ad_max, when):
			return 'Dopo cena'


def urightparse(f, enc=None):
	"""Parse the file exported by the Uright windows applications.

	Args:
		f(string)   the file name to parse
		enc(string) the file encoding if known else it is detected by chardet
	Returns:
		a list of tuples or dictionaries with all I need
"""
	if enc == None:
		enc = getencoding(f)

		clean_input = str.maketrans('./', ':-', ' ="')
	measurements = []

    with open(f, 'r', encoding=enc) as badcsv:
        rows = csv.reader(badcsv, delimiter="\t")
        next(rows, None)  # Skip first line that has column names

        for row in rows:
	        m_date = row[1].translate(clean_input)
	        m_time = row[2].translate(clean_input)
	        m_level = row[3].translate(clean_input)
	        m_type = set_mtype(m_time, row[5].translate(clean_input))

	        measurements.append((m_date, m_time, m_level, m_type))
        return measurements


def reshape(measurements):
	new_rows = {}

	for row in measurements:

		if not row[0] in new_rows.keys():
			new_rows[row[0]] = ((row[1], row[2], row[3]),)
		else:
			new_rows[row[0]] += ((row[1], row[2], row[3]),)

	pprint(new_rows)


def pget(f):
	"""Get data using Pandas."""
	df = pd.read_table(f, encoding='UTF-16', usecols=[1, 2, 3, 5],
	                   index_col=False)
	df.columns = ['date', 'time', 'level', 'type']
	clean_input = str.maketrans('', '', ' ="')
	df = df.applymap(lambda x: str(x).translate(clean_input))
	df['level'] = pd.to_numeric(df['level'])
	df['i'] = pd.to_datetime(df['date'] + ' ' + df['time'],
	                         format='%Y/%m/%d %H:%M')
	df.set_index('i', inplace=True)
	df.sort_values(['date', 'time'], ascending=[False, True], inplace=True)

	# TODO: Add column to categorize levels by period of day

	print(df.head(20))


# print(df.dtypes)
# print(df[df['level'] < 120])  # <-- Filter example!!!
# print(df['level'].between_time('04:30', '10:30'))
# print(df[:'2018-03-10'])


# Testing
filetoread = '/home/glsg/Projects/glicemix/20180510-all.csv'
enc = getencoding(filetoread)
meas = urightparse(filetoread, enc)
pprint(meas)
