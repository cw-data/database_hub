# SQL and python to create a fresh sqlite db for app.py
# CAUTION!!!!!!!!!!!!!!!!
# Running this script deletes all data currently stored in the db

import sqlite3

connection = sqlite3.connect('fish_db.sqlite')
cursor = connection.cursor()
# tbl_sample
cursor.execute('DROP TABLE IF EXISTS tbl_sample')
cursor.execute('''CREATE TABLE "tbl_sample" (
	"spl_id"	TEXT NOT NULL UNIQUE,
	"spl_datetime"	TEXT NOT NULL,
	"pool"	TEXT NOT NULL,
	"gear"	TEXT NOT NULL,
	"latitude_real"	REAL NOT NULL,
	"longitude_real"	REAL NOT NULL,
	"latitude_numeric"	NUMERIC NOT NULL,
	"longitude_numeric"	NUMERIC NOT NULL,
	PRIMARY KEY("spl_id")
)''')

# tbl_fish
cursor.execute('DROP TABLE IF EXISTS tbl_fish')

cursor.execute('''CREATE TABLE "tbl_fish" (
    "spl_ID"	INTEGER NOT NULL,
	"fsh_ID"	INTEGER NOT NULL UNIQUE,
	"species_code"	TEXT NOT NULL,
	"length_mm"	INTEGER,
	"weight_g"	INTEGER,
	FOREIGN KEY("spl_ID") REFERENCES "tbl_sample"("spl_id"),
	PRIMARY KEY("fsh_ID")
)''')

# a test record
connection = sqlite3.connect('fish_db.sqlite')
cursor = connection.cursor()
cursor.execute("INSERT INTO tbl_sample (spl_id, spl_datetime, pool, gear, latitude_real, longitude_real, "
               "latitude_numeric, longitude_numeric) VALUES (9, 10, 11, 12, 13, 14, 15, 16)")
connection.commit()
connection.close()

# test data
data = [{'spl_id': 'Romina', 'spl_datetime': '2020-07-10 15:00:00.000', 'pool': 'DI', 'gear': 'EF',
         'latitude_real': 88.123456, 'longitude_real': 45.123456, 'latitude_numeric': 88.123456,
         'longitude_numeric': 45.123456}]

import pandas as pd
df = pd.read_csv('sample_data.csv', sep=',')

fname = input('Enter file name or path')
if (len(fname) < 1): fname = 'sample_data.txt'
fh = open(fname)
for line in fh:
    pieces = line.split()
    print(pieces)

cursor.close()
