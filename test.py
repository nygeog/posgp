import psycopg2
import posgp
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


posgp.printTest('connected')



posgp.printCensusTractGEOIDS('36')
