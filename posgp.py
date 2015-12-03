###    ##    ###   ###    ###
#  #  #  #  #     #       #  #
###   #  #  ####  #   ##  ###
#     #  #     #  #   #   #
#      ##   ###    ###    #
import urllib
import urllib2
import time
#import sqlalchemy - maybe don't need
import psycopg2


#def posgpAuthenticate():

def printTest(inText):
	print inText + ' posgp.py - printTest'

def printCensusTractGEOIDS(inState,dbname,user,host,password):
	#try:
	conn = psycopg2.connect("dbname='"+dbname+"' user='"+user+"' host='"+host+"' password='"+password+"'")
	cur = conn.cursor()
	cur.execute("""SELECT geoid10 from tracts_2010_state_"""+inState)
	rows = cur.fetchall()
	print "\nShow me the census tracts:\n"
	for row in rows:
		print "   ", row[0]

	# except:
	# 	print "I am unable to connect to the database"



# def createTable(table_name,username,apikey): #add a field for a dictionary of fields and field types you want to add
# 	url = "https://%s.cartodb.com/api/v1/sql" % username
# 	insertList = ["CREATE TABLE "+table_name+" (uid int);",
# 	"SELECT cdb_cartodbfytable('"+table_name+"');"]
# 	for pauser, insert in enumerate(insertList): 
# 		params = {'api_key' : apikey,'q' : insert}  
# 	    	print insert
# 	    	req = urllib2.Request(url, urllib.urlencode(params))
# 	    	response = urllib2.urlopen(req)
# 	    	print '-' * (pauser + 1)
# 	    	time.sleep(2)
  
#def addPoints(table_name):

# def buffer(in_buffer,buffer_dist,ou_buffer,username,apikey):  	
# 	# "CREATE TABLE latlngtablebuffer_"+fd+" AS SELECT ST_Buffer(the_geom_webmercator, "+bufDist+") AS the_geom_webmercator, cartodb_id, cdbawcensusuid FROM latlngtable_"+fd+"",
#     # "SELECT cdb_cartodbfytable('latlngtablebuffer_"+fd+"');",
# 	"CREATE TABLE "+ou_buffer+" AS SELECT ST_Buffer(the_geom_webmercator, "+buffer_dist+") AS * FROM "+in_buffer


#def intersect(intables,outtables,infields):
