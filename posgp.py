###    ##    ###   ###    ###
#  #  #  #  #     #       #  #
###   #  #  ####  #   ##  ###
#     #  #     #  #   #   #
#      ##   ###    ###    #
import urllib
import urllib2
import time
import sqlalchemy

def printTest(inText):
	print inText + ' posgp.py - printTest'

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
# 	"CREATE TABLE latlngtablebuffer_"+fd+" AS SELECT ST_Buffer(the_geom_webmercator, "+bufDist+") AS the_geom_webmercator, cartodb_id, cdbawcensusuid FROM latlngtable_"+fd+"",
#     "SELECT cdb_cartodbfytable('latlngtablebuffer_"+fd+"');",

#def intersect(intables,outtables,infields):
