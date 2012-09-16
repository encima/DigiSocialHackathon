import sqlite3 as sql

def print_tables():
	print "hello"

def get_data(table, lhb, cursor, field):
	query = "SELECT * FROM " + table + " WHERE "+ field +" = '" + str(lhb) + "';"
	cursor.execute(query)
	result = cursor.fetchall()
	for res in result:
		print res

def rreplace(s, old, new, occurrence):
	li = s.rsplit(old, occurrence)
	return new.join(li)

conn = sql.connect('/Users/encima/Dropbox/Projects/digisocial/wales_health_data.sqlite')

cur = conn.cursor()
#Get all tables in database
cur.execute("""SELECT name FROM sqlite_master WHERE type='table' ORDER BY name""")

result = cur.fetchall()
#Loop through tables and request data for all lhb (health boards)
tables =''
for res in result:
	table_name = res[0]
	cur.execute("PRAGMA table_info(" + table_name + ")")
	result = cur.fetchall()
	tables += "'" + table_name + "', "
	print table_name
	print '---------'
	# print "@attributer " + row[1] + " real"
	for res in result: print res[1] + ',',
	print '---------'
	for i in range(1, 8):
		if('lhb' in result[0][1]):
			get_data(table_name, i, cur, 'lhb')
		else:
			print result
			# get_data(table_name, i, cur, 'id')
	print '---------'

# tables = rreplace(tables, ',', '', 1)
# print tables
# query = "SELECT * FROM " + tables + " WHERE lhb = '1';"
# cur.execute(query)
# result = cursor.fetchall()
# for res in result:
# 	print res


		