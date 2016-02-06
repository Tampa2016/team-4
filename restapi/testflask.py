#DB Schema
#0	Streetname		3   name       6	Latitude
#1  Address Number	4	Rating
#2  ZIP				5   Longitude

from flask import Flask, request
from flask_restful import Resource, Api

import json

DEBUG = True

import _mysql



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

def accessDB(inputQuery):
	con = _mysql.connect(host="localhost", user="root", passwd="code4good", db="team4")
	con.query(inputQuery)

	return con

def searchDBName(inputName):

	nameQuery = "SELECT * FROM locations WHERE LOCATIONNAME = "
	nameQuery += "\'"
	nameQuery += inputName
	nameQuery += "\'"

	print nameQuery


	#con = _mysql.connect(host="localhost", user="root", passwd="code4good", db="team4")
	#con.query(nameQuery)
	
	#Access the DB and store result, return it
	results = accessDB(nameQuery).store_result()

	return results

def searchDBLocation(log, lat):
		#Search range in terms of longitude and lattitude
		longSearchPlus = log + 0.5000
		longSearchMin = log - 0.5000

		latSearchPlus = lat + 0.5000
		latSearchMin = lat - 0.5000

#		locationQuery = "SELECT * from location WHERE ((LONGITUDE BETWEEN " + logSearchPlus + " AND " + logSearchMin ") AND (LATITUDE BETWEEN " + latSearchPlus + " AND " + latSearchMin + "))"

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



def formatJSON(inputResults):

	rows = inputResults.fetch_row()
	print rows

	dataItem = {}

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
		



#TODO DEBUG MULTIPLE VAR INPUT JSON
class SearchByLocation(Resource):
	#Example curl request
	# curl http://127.0.0.1:5000/searchLocation?longitude=27.986800173&latitude:-82.328399309
	def get(self):
		longitude = request.args['longitude']
		latitude = request.args['latitude']


		results = SearchByLocation()
		json_data = formatJSON(results)


		return json_data



api.add_resource(HelloWorld, '/')
api.add_resource(ConnectDBTest, '/DBT')
api.add_resource(SearchByLocation, '/searchLocation')
api.add_resource(SearchByName, '/searchName')

if __name__ == '__main__':
	app.run(debug=True)

