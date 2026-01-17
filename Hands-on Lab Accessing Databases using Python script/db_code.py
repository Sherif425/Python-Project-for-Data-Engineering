import sqlite3
import pandas as pd

conn = sqlite3.connct('STAFF.db')

table_name = 'INSTRUCTOR'
attribute_list = ['ID', 'FNAME', 'LNAME', 'CITY', 'CODE']



