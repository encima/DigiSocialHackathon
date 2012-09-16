import sqlite3,StringIO,re


class db:
    def __init__(self, loc, table, fields):
        self.conn = sqlite3.connect(loc)
        self.setupDB(table,fields)

    def commit(self):
        self.conn.commit()

    def close(self):
        self.conn.close()

    def get_lhb_id(self,s):
        c = self.conn.cursor()
        q = "select id from local_health_boards where name like '%s'" %(s.replace("'","''"))
        c.execute(q)
        res = c.fetchone()
        return res[0]

    def setupDB(self,table,fields):
        #q = "create table if not exists bed_avail('lhb' INTEGER,'acute' INTEGER, 'maternity' INTEGER, 'geriatrics' INTEGER, 'nonpsych' INTEGER, 'psych' INTEGER, 'total' INTEGER);"
        q = "create table if not exists %s ('lhb' INTEGER"%(table)
        for a in fields:
            q = q+", '%s' %s"%(a[0],a[1])
        q = q+");"
        c = self.conn.cursor()
        print q
        c.execute(q)
        self.commit()

    def insert(self,l, table,fieldcount):
        c = self.conn.cursor()
        q = "INSERT INTO %s VALUES(" %(table)
        q = q+"?"
        for a in range(1,fieldcount):
            q=q+", ?"
        q = q+");"
        c.executemany(q,l)
        self.commit()

    


def fix(s):
    return re.sub("\\t+","\\t",s)

tab = "A_and_E_times_10_11"
fields = [
    ["all_attendences","INTEGER"],
    ["all_lt_4_hrs_pc","FLOAT"],
    ["all_lt_8_hrs_pc","FLOAT"],
    ["maj_attendences","INTEGER"],
    ["maj_lt_4_hrs_pc","FLOAT"],
    ["maj_lt_8_hrs_pc","FLOAT"],
    
    ]

conn = db("C:\\Users\\mgreenwood\\Dropbox\\digisocial\\wales_health_data.sqlite",tab,fields)

text = """  Betsi Cadwaladr University			214,225		89.6		98.7		165,872		86.9		98.4
  Powys Teaching			15,573		99.8		100.0		.		.		.
  Hywel Dda			142,944		88.5		97.8		99,148		87.5		97.7
  Abertawe Bro Morgannwg University			186,049		85.2		95.9		141,750		82.7		95.3
  Cwm Taf			129,157		90.4		97.1		106,468		88.4		96.5
  Aneurin Bevan			162,221		88.3		96.2		131,628		85.7		95.3
  Cardiff and Vale University			133,921		85.5		96.5		125,158		84.5		96.3"""
buf = StringIO.StringIO(text)
a = buf.readline()
rec = list()
while (len(a)>0):
    temp = fix(a.strip()).split("\t")
    temp[0] = str(conn.get_lhb_id(temp[0].strip()))
    for b in range(len(temp)):
        temp[b] = temp[b].replace(",","")
        if temp[b].isdigit():
            temp[b]=int(temp[b])
    print temp
    rec.append(temp)
    a = buf.readline()
conn.insert(rec,tab,len(fields)+1)
