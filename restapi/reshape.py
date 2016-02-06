#DB Schema
#0	Streetname		3   name       6	Latitude     	9   Bathroom 	12 	Curbs 		15 	Velco
#1  Address Number	4	Rating     7	Ramps 			10	Pool Lifts 	13 	Shuttle 	16 	Temp
#2  ZIP				5   Longitude  8    Toilet Height	11	Restaurant	14 	Lifts		17 	Door Width

#Restful API to Access database from outside. 
#Current available functions
#searchByLocation given longitude and latitude
#searchByName given a business name
#AddNewItem given an HTTP request with arguements

#to start install Flask
# python restapi.py

from flask import Flask, request
from flask_restful import Resource, Api

import json

DEBUG = True

import _mysql

dbDataValues = {'0':'streetname',
				'1':'streetnumber',
				'2':'zip',
				'3':'name',
				'4':'rating',
				'5':'longitude',
				'6':'latitude',
				'7':'ramp',
				'8':'toiletheight',
				'9':'bathroom',
				'10':'poollifts',
				'11':'restaurant',
				'12':'curbs',
				'13':'shuttle',
				'14':'lifts',
				'15':'velcro',
				'16':'temp',
				'17':'doorwidth'}
dataItemsList = {'streetname',
				'streetnumber',
				'zip',
				'name',
				'rating',
				'longitude',
				'latitude',
				'ramp',
				'toiletheight',
				'bathroom',
				'poollifts',
				'restaurant',
				'curbs'
				'shuttle',
				'lifts',
				'velcro',
				'temp',
				'doorwidth'}

qq = "SELECT * FROM locations"

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
	def get(self):
		print "helloworld"
		return {'hello': 'world'}


class ConnectDBTest(Resource):
	def get(self):

		con = _mysql.connect(host="localhost", user="root", passwd="code4good", db="team4")

		con.query(qq)

		results = con.use_result()

		for result in results:
			print result["name"]

		return {'TestDB': 'Successful'}

def accessDBQuery(inputQuery):
	#Access MySQL DB given an input query, string
	con = _mysql.connect(host="localhost", user="root", passwd="code4good", db="team4")
	con.query(inputQuery)

	return con

def accessDB():
	#Access MySQL DB given an input query, string
	con = _mysql.connect(host="localhost", user="root", passwd="code4good", db="team4")

	return con

def searchDBName(inputName):

	nameQuery = "SELECT * FROM locations WHERE LOCATIONNAME = "
	nameQuery += "\'"
	nameQuery += inputName
	nameQuery += "\'"

	print nameQuery
	
	#Access the DB and store result, return it
	results = accessDBQuery(nameQuery).store_result()

	return results

def searchDBLocation(log, lat):
		#Search range in terms of longitude and lattitude
		longSearchPlus = log + 0.5000
		longSearchMin = log - 0.5000

		latSearchPlus = lat + 0.5000
		latSearchMin = lat - 0.5000

		#locationQuery = "SELECT * from location WHERE ((LONGITUDE BETWEEN " + logSearchPlus + " AND " + logSearchMin ") AND (LATITUDE BETWEEN " + latSearchPlus + " AND " + latSearchMin + "))"

		#Build the query
		#Probably uncessary work but tried and true so far so oh well
		locationQuery = "SELECT * from location WHERE ((LONGITUDE BETWEEN " 
		locationQuery += "\'"
		locationQuery += logSearchPlus
		locationQuery += "\'"
		locationQuery += " AND "
		locationQuery += "\'"
		locationQuery += logSearchMin
		locationQuery += "\'"
		locationQuery += ") AND LATITUDE BETWEEN "
		locationQuery += "\'"
		locationQuery += latSearchPlus
		locationQuery += "\'"
		locationQuery += " AND "
		locationQuery += "\'"
		locationQuery += latSearchMind
		locationQuery += "\'"
		locationQuery += "))"

		print locationQuery

		results = accessDB(locationQuery).store_result()

		return results





def addToDB(request):
	#Access MySQL DB given an input query, string
	con = _mysql.connect(host="localhost", user="root", passwd="code4good", db="team4")

	cur = con.cursor()
	cur.execute("CREATE ")

	#for every arguement supplied, check if it matches the list of possible
	#valid data types, if it matches, build an insertion query and execute it
	#into the database

	namesToInsert = "("
	valuesToInsert = "("

	for item in request:
		for dbt in dataItemsList:
			if item[dbt] != NULL:
				#con.execute(insertionQueryBuilder(dbt, item[dbt]))
				namesToInsert += dbt
				namesToInsert += ", "
				valuesToInsert += "\'"
				valuesToInsert += item[dbt]
				valuesToInsert += "\'"
				valuesToInsert += ", "

	#remove last comma
	namesToInsert = namesToInsert[:-1]
	valuesToInsert = valuesToInsert[:-1]

	#finish building insertion query
	namesToInsert += ")"
	valuesToInsert += ")"
	
	query = "INSERT INTO locations "
	query += namesToInsert
	query += " VALUES "
	query += valuesToInsert

	print query


	#DEBUG CURSOR WRONG ATTRIBUTE
	cur.execute(query)



#TODO: Add the new database item tables
def formatJSON(inputResults):
	#input results from a mysql query
	#return a json-formatted object
	rows = inputResults.fetch_row()
	print rows

	dataItem = {}


	#TODO: Add the new database item tables
	for row in rows: 
		dataItem["streetname"] = row[0]
		dataItem["addressnumber"] = row[1]
		dataItem["zip"] = row[2]
		dataItem["name"] = row[3]
		dataItem["rating"] = row[4]
		dataItem["longitude"] = row[5]
		dataItem["latitude"] = row[6]



	json_data_final = json.dumps(dataItem)

	print json_data_final
	return json_data_final


class SearchByName(Resource):		
	def get(set):
		#Example curl request
		# curl http://127.0.0.1:5000/searchName?name=starbucks

		#request comes in, grab name varable
		recvName = request.args['name']

		results = searchDBName(recvName)	
		json_data = formatJSON(results)

		return json_data
		

class SearchByLocation(Resource):
	#Example curl request
	# curl http://127.0.0.1:5000/searchLocation?longitude=27.986800173&latitude:-82.328399309
	def get(self):
		longitude = request.args['longitude']
		latitude = request.args['latitude']


		results = SearchByLocation()
		json_data = formatJSON(results)


		return json_data

class AddNewItem(Resource):
	#Add a new item to the database
	#CURL example
	#longitude=27.986800173&latitude:-82.328399309
	# curl -X PUT -d "streetname=highland" -d "streetnumber=5422" -d "zip=33945" -d "name=Chase" -d "ramp=1" -d "toiletheight=32" -d "poollift=1" -d "shuttle=1" http://127.0.0.1:5000/addNewItem

	def put(self):
		addToDB(request)





#Routing API Declarations
#e.g. host/searchLocation calls the searchByLocation class
api.add_resource(HelloWorld, '/')
api.add_resource(ConnectDBTest, '/DBT')
api.add_resource(SearchByLocation, '/searchLocation')
api.add_resource(SearchByName, '/searchName')
api.add_resource(AddNewItem, '/addNewItem')

if __name__ == '__main__':
	app.run(debug=True)

