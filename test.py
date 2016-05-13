import psycopg2
import posgp
import _secret_info

dbname   = _secret_info.s_dbname
user     = _secret_info.s_user
host     = _secret_info.s_host
password = _secret_info.s_password

posgp.printCensusTractGEOIDS('21',dbname,user,host,password)

