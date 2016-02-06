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


class SearchByName(Resource):
	def put(self):
		print request
		recvName = request.form['name']

		
		nameQuery = "SELECT * FROM locations WHERE LOCATIONNAME = "
		nameQuery += "\'"
		nameQuery += recvName
		nameQuery += "\'"

		print nameQuery


		con = _mysql.connect(host="localhost", user="root", passwd="code4good", db="team4")
		con.query(nameQuery)

		results = con.store_result()

		rows = results.fetch_row()
		print rows

		data = {}
		

		for row in rows: 
			dataItem = {}

			dataItem['streetname'] = row[0]
			dataItem['addressnumber'] = row[1]
			dataItem['zip'] = row[2]
			dataItem['name'] = row[3]
			dataItem['rating'] = row[4]
			dataItem['longitude'] = row[5]
			dataItem['latitude'] = row[6]

			json_data = json.dumps(dataItem);
			data += json_data

		print data

		json_data_final = json.dumps(data)

		print json_data_final

		print rows

		return json_data_final
		


	#curl --data "param1=value1&param2=value2" https://example.com/resource.cgi
	#curl --data "name=starbucks" http://127.0.0.1:5000/searchName
	#curl -X PUT -d arg=val -d arg2=val2 localhost:8080
	#curl -X PUT -d 'name=starbucks' http://127.0.0.1:5000/searchName
	#curk http://127.0.0.1:5000/searchName - "data"

#TODO DEBUG MULTIPLE VAR INPUT JSON
class SearchByLocation(Resource):
	def put(self):
		#Get location Long / Lat by JSON Object from HTTP PUT Req
		data = request.form['data']

		log = data.form['log']
		lat = data.form['lat']

		print log + " " + lat

		#27.986800173,	-82.328399309
		#Search range 
		logSearchPlus = log + 0.5000
		latSearchPlus = lat + 0.5000

		logSearchMin = log - 0.5000
		latSearchMin = lat - 0.5000

#		locationQuery = "SELECT * from location WHERE ((LONGITUDE BETWEEN " + logSearchPlus + " AND " + logSearchMin ") AND (LATITUDE BETWEEN " + latSearchPlus + " AND " + latSearchMin + "))"

		con = _mysql.connect(host="localhost", user="root", passwd="code4good", db="team4")
		con.query(locationQuery)

		results = con.use_result()

		for result in results:
			print result["name"]

		return {'TestByLocation': 'Successful'}


#curl -X PUT -d log=27.980000 -d lat=-82.320000 127.0.0.1:5000/searchLoc
#curl -X PUT -d log=27.980000 -d lat=-82.320000 127.0.0.1:5000/searchLoc
#curl -X PUT -H "Content-Type: application/json" -d '{"log":"27.98000"}, {"lat":"-82.32000"}' 127.0.0.1:5000/searchLoc

api.add_resource(HelloWorld, '/')
api.add_resource(ConnectDBTest, '/DBT')
api.add_resource(SearchByLocation, '/searchLoc')
api.add_resource(SearchByName, '/searchName')

if __name__ == '__main__':
	app.run(debug=True)

