import sqlite3 as sql

def get_data(table, lhb, cursor, field):
	query = "SELECT * FROM " + table + " WHERE "+ field +" = '" + str(lhb) + "';"
	cursor.execute(query)
	result = cursor.fetchall()
	for res in result:
		for r in res:
			print r

def rreplace(s, old, new, occurrence):
	li = s.rsplit(old, occurrence)
	return new.join(li)

conn = sql.connect('/Users/encima/Dropbox/Projects/digisocial/wales_health_data.sqlite')

cur = conn.cursor()

#Get all tables in database
cur.execute("""SELECT name FROM sqlite_master WHERE type='table' ORDER BY name""")

tables = cur.fetchall()
all_tabs = ''
all_cols = ''
for table in tables:
	all_tabs += table[0] + ', '
	cur.execute("PRAGMA table_info(" + table[0] + ")")
	columns = cur.fetchall()
	for column in columns:
		all_cols += "'" + table[0] + '.' + column[1] + "', "
	# 	# if 'lhb' not in column[1]:
	# 	# 	print "@attribute " + column[1] + " real"
	# 	for i in range(1, 8):
	# 		if 'lhb' in column[1]:
	# 			# print 'Selecting using lhb'
	# 			get_data(table[0], i, cur, 'lhb')
	# 		elif 'id' in columns[1]:
	# 			# print 'Selecting using ID'
	# 			get_data(table[0], i, cur, 'i')

# rreplace(all_tabs, ',', '', 2)
# rreplace(all_cols, ',', '', 2)
all_tabs = all_tabs[::-1].replace(","[::-1], ""[::-1], 1)[::-1]
all_cols = all_cols[::-1].replace(","[::-1], ""[::-1], 1)[::-1]

query = "SELECT " + all_cols + "FROM " + all_tabs + "WHERE A_and_E_times_10_11.lhb = '1';"
cur.execute(query) 
data = cur.fetchall()

for d in data:
	print d