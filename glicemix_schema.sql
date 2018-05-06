BEGIN TRANSACTION;
PRAGMA application_id = 170379 ;
CREATE TABLE IF NOT EXISTS settings (
	setting_key    TEXT,
	setting_value  TEXT
);
CREATE TABLE IF NOT EXISTS measurements (
	m_date	TEXT(10),
	m_time	TEXT(5),
	m_level	INTEGER,
	m_type	TEXT(20),
	PRIMARY KEY(m_date,m_time)
) WITHOUT ROWID;
CREATE TABLE IF NOT EXISTS insuline (
	i_date	TEXT(10),
	i_time	TEXT(5),
	units	INTEGER,
	i_type	TEXT(20),
	PRIMARY KEY(i_date,i_time)
) WITHOUT ROWID;
CREATE TABLE IF NOT EXISTS day_info (
	day        TEXT(10),
	day_type   TEXT(20),
	PRIMARY KEY(day)
) WITHOUT ROWID;
COMMIT;
