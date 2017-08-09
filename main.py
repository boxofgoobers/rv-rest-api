from flask import Flask 
from flask_restful import Api
from resources import CityResource, CityGeoResource, \
			StateResource, StateCityResource, \
			UserResource, VisitResource

app = Flask(__name__)
api = Api(app)
api.add_resource(CityResource,      '/city',  '/city/<id>')
api.add_resource(StateResource,	    '/state', '/state/<id>')
api.add_resource(StateCityResource, '/state/<state>/cities')   # 1. GET  List all cities in a state
api.add_resource(UserResource,      '/user',  '/user/<id>')
api.add_resource(VisitResource,
		'/visits',
		'/user/<id>/visits',            # 4. GET  Return a list of cities the user has visited
										# 2. POST Allow to create rows of data to indicate they have visited a particular city.
		'/user/<id>/visit/states',      # 5. GET  Return a list of states the user has visited
		'/user/<id>/visit/<visit_id>'   # 3. DEL  Allow a user to remove an improperly pinned visit.
	)
api.add_resource(CityGeoResource,
		'/city/<id>/geo')  # GET  Bonus: Fetch geo data using latitude / longitude data


@app.route('/', methods=['GET'])
def hello():
    return 'How you doin?!'


if __name__ == '__main__':
    app.run(debug=True)
