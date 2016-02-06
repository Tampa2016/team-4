from flask import Flask
from flask_restful import Resource, Api

DEBUG = True

import _mysql

db = _mysql.connect(host="localhost", user="root", passwd="code4good", db="locations")

qq = 'SELECT * FROM locations'


app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
	def get(self):
		log("helloworld")
		return {'hello': 'world'}


class ConnectDBTest(Resource):
	def get(self):

		db.query(qq)

		r = db.store_result()

		r.fetch_row(5)

		
		db.close()

		return {'test': 'db'}


api.add_resource(HelloWorld, '/')
api.add_resource(ConnectDBTest, '/DBT')

if __name__ == '__main__':
	app.run(debug=True)

