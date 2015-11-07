import psycopg2
import _secret_info

dbname   = _secret_info.s_dbname
user     = _secret_info.s_user
host     = _secret_info.s_host
password = _secret_info.s_password

try:
    conn = psycopg2.connect("dbname='"+dbname+"' user='"+user+"' host='"+host+"' password='"+password+"'")
except:
    print "I am unable to connect to the database"

cur = conn.cursor()

cur.execute("""SELECT geoid10 from tracts_2010_state_01""")

rows = cur.fetchall()

print "\nShow me the databases:\n"
for row in rows:
    print "   ", row[0]


