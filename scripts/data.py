import sqlite3,StringIO,re


class db:
    def __init__(self, loc):
        self.conn = sqlite3.connect(loc)
        self.setupDB()

    def commit(self):
        self.conn.commit()

    def close(self):
        self.conn.close()

    def setupDB(self):
        query = "create table if not exists bed_avail('lhb' INTEGER,'acute' INTEGER, 'maternity' INTEGER, 'geriatrics' INTEGER, 'psych' INTEGER, 'total' INTEGER);"
        c = self.conn.cursor()
        c.execute(q)
        self.commit()


def fix(s):
    return re.sub("\\t+","\\t",s)

text = """Betsi Cadwaladr University			1,679		115		543		2,336		408		2,744
Powys Teaching 			98		11		103		213		65		278
Hywel Dda			978		56		102		1,136		161		1,297
Abertawe Bro Morgannwg University			1,619		101		268		1,988		639		2,627
Cwm Taf			1,031		80		278		1,390		271		1,662
Aneurin Bevan			1,276		91		247		1,665		286		1,951
Cardiff and Vale University			1,716		83		81		1,881		377		2,258
"""
buf = StringIO.StringIO(text)
a = buf.readline()
while (len(a)>0):
    temp = fix(a.strip()).split("\t")
    print temp
    a = buf.readline()
