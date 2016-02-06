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
	def put(self, name):
		recvName = request.form['data']
		data = {}

		nameQuery = "SELECT * from location WHERE LOCATIONAME = " + recvName

		con = _mysql.connect(host="localhost", user="root", passwd="code4good", db="team4")
		con.query(nameQuery)

		results = con.use_result()

		for result in results:
			data['name'] = result['name']
			print result['name']

		return data

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

		locationQuery = "SELECT * from location WHERE ((LONGITUDE BETWEEN " + logSearchPlus + " AND " + logSearchMin ") AND (LATITUDE BETWEEN " + latSearchPlus + " AND " + latSearchMin + "))"

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

if __name__ == '__main__':
	app.run(debug=True)

