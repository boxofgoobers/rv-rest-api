import requests
from flask import request
from flask_restful import Resource, Api
from services import CityService, StateService, StateCityService, UserService, VisitService


class CityResource(Resource):
	def get(self, id=None):
		try:
			if id is None:
				(status, data) = CityService().read_all()
				return {'status': status, 'data': data}
			else:
				(status, data) = CityService().read(id=id)
				return {'status': status,
					'data': data.to_json() if callable(getattr(data, "to_json", None)) else str(data)}

		except Exception as x:
			return {'status': False, 'message': str(x)}


	# def post(self):
	# 	try:
	# 		name      = request.form.get('name')
	# 		state_id  = request.form.get('state_id')
	# 		status    = request.form.get('status')
	# 		latitude  = request.form.get('latitude')
	# 		longitude = request.form.get('longitude')

	# 		if name is None:
	# 			return { 'status': False, 'message': 'Name is required.' }
	# 		if state_id is None:
	# 			return { 'status': False, 'message': 'State ID is required.' }
	# 		if status is None:
	# 			return { 'status': False, 'message': 'Status is required.' }
	# 		if latitude is None:
	# 			return { 'status': False, 'message': 'Latitude is required.' }
	# 		if longitude is None:
	# 			return { 'status': False, 'message': 'Longitude is required.' }

	# 		(status, city) = CityService().create(name, state_id, status, latitude, longitude)
	# 		return { 'status': status,
	# 				'message': 'City has been added.' if status else 'An error exists',
	# 				'data': city.to_json()}

	# 	except Exception as x:
	# 		return {'status': False, 'message': str(x)}


	# def put(self, id=None):
	# 	try:
	# 		if id is None:
	# 			return { 'status': False, 'message': 'City Id is required.' }
	# 		else:
	# 			name      = request.form.get('name')
	# 			state_id  = request.form.get('state_id')
	# 			status    = request.form.get('status')
	# 			latitude  = request.form.get('latitude')
	# 			longitude = request.form.get('longitude')

	# 			if name is None and state_id is None and status is None\
	# 							and latitude is None and longitude is None:
	# 				return { 'status': True, 'message': 'Nothing to update!' }
	# 			else:
	# 				(status, city) = CityService().update(name, state_id, status, latitude, longitude)
	# 				return { 'status': status,
	# 						'message': 'City has been updated.' if status else 'An error exists',
	# 						'data': city.to_json()}

	# 	except Exception as x:
	# 		return {'status': False, 'error': str(x)}


	# def delete(self, id=None):
	# 	try:
	# 		if id is None:
	# 			return { 'status': False, 'message': 'City Id is required.' }
	# 		else:
	# 			(status, city) = CityService().delete(id)
	# 			return { 'status': status,
	# 					'message': 'City has been deleted.' if status else 'An error exists',
	# 					'data': city.to_json() }

	# 	except Exception as x:
	# 		return {'status': False, 'error': str(x)}


class StateCityResource(Resource):
	def get(self, state=None):
		try:
			(status, data) = StateCityService().read(state)
			return {'status': status,
				'data': data.to_json() if callable(getattr(data, "to_json", None)) else data}

		except Exception as x:
			return {'status': False, 'message': str(x)}


class StateResource(Resource):
	def get(self, id=None):
		try:
			if id is None:
				(status, data) = StateService().read_all()
				return {'status': status, 'data': data}
			else:
				(status, data) = StateService().read(id=id)
				return {'status': status,
					'data': data.to_json() if callable(getattr(data, "to_json", None)) else str(data)}

		except Exception as x:
			return {'status': False, 'message': str(x)}


	# def post(self):
	# 	try:
	# 		name         = request.form.get('name')
	# 		abbreviation = request.form.get('abbreviation')

	# 		if name is None or abbreviation is None:
	# 			return { 'status': False, 'message': 'Name and Abbreviation are required.' }

	# 		(status, state) = StateService().create(name, abbreviation)
	# 		return { 'status': status,
	# 				'message': 'State has been added.' if status else 'An error exists',
	# 				'data': state.to_json()}

	# 	except Exception as x:
	# 		return {'status': False, 'message': str(x)}


	# def put(self, id=None):
	# 	try:
	# 		if id is None:
	# 			return { 'status': False, 'message': 'State Id is required.' }
	# 		else:
	# 			name         = request.form.get('name')
	# 			abbreviation = request.form.get('abbreviation')

	# 			if name is None and abbreviation is None:
	# 				return { 'status': True, 'message': 'Nothing to update!' }
	# 			else:
	# 				(status, user) = StateService().update(first_name, last_name)
	# 				return { 'status': status,
	# 						'message': 'User has been updated.' if status else 'An error exists',
	# 						'data': user.to_json() }

	# 	except Exception as x:
	# 		return {'status': False, 'error': str(x)}

	# def delete(self, id=None):
	# 	try:
	# 		if id is None:
	# 			return { 'status': False, 'message': 'User Id is required.' }
	# 		else:
	# 			(status, user) = StateService().delete(id)
	# 			return { 'status': status,
	# 					'message': 'User has been deleted.' if status else 'An error exists',
	# 					'data': user.to_json() }

	# 	except Exception as x:
	# 		return {'status': False, 'error': str(x)}



class UserResource(Resource):
	def get(self, id=None):
		try:
			if id is None:
				(status, data) = UserService().read_all()
				return {'status': status, 'data': data}
			else:
				(status, data) = UserService().read(id)
				return {'status': status,
					'data': data.to_json() if callable(getattr(data, "to_json", None)) else str(data)}

		except Exception as x:
			return {'status': False, 'message': str(x)}


	def post(self):
		try:
			first_name = request.form.get('first_name')
			last_name  = request.form.get('last_name')

			if first_name is None or last_name is None:
				return { 'status': False, 'message': 'First and Last Name are required.' }

			(status, user) = UserService().create(first_name, last_name)
			return { 'status': status,
					'message': 'User has been added.' if status else 'An error exists',
					'data': user.to_json()}

		except Exception as x:
			return {'status': False, 'message': str(x)}


	# def put(self, id=None):
	# 	try:
	# 		if id is None:
	# 			return { 'status': False, 'message': 'User Id is required.' }
	# 		else:
	# 			first_name = request.form.get('first_name')
	# 			last_name  = request.form.get('last_name')

	# 			if first_name is None and last_name is None:
	# 				return { 'status': True, 'message': 'Nothing to update!' }
	# 			else:
	# 				(status, user) = UserService().update(first_name, last_name)
	# 				return { 'status': status,
	# 						'message': 'User has been updated.' if status else 'An error exists',
	# 						'data': user.to_json() }

	# 	except Exception as x:
	# 		return {'status': False, 'error': str(x)}


	# def delete(self, id=None):
	# 	try:
	# 		if id is None:
	# 			return { 'status': False, 'message': 'User Id is required.' }
	# 		else:
	# 			(status, user) = UserService().delete(id)
	# 			return { 'status': status,
	# 					'message': 'User has been deleted.' if status else 'An error exists',
	# 					'data': user.to_json() }

	# 	except Exception as x:
	# 		return {'status': False, 'error': str(x)}


class VisitResource(Resource):
	def get(self, id=None):
		cities_request = request.url.endswith('/visits')
		states_request = request.url.endswith('/visit/states')

		try:
			if id is not None:
				if cities_request:
					(status, data) = VisitService().read_cities_visited(id)
					return {'status': status, 'data': data}
				elif states_request:
					(status, data) = VisitService().read_states_visited(id)
					return {'status': status, 'data': data}
			else:
				(status, data) = VisitService().read_all()
				return {'status': status, 'data': data}

		except Exception as x:
			return {'status': False, 'message': str(x)}

	def post(self, id=None):
		try:
			state = request.form.get('state')
			city  = request.form.get('city')

			if id is None or state is None or city is None:
				return { 'status': False, 'message': 'User id, State and City are required.' }

			if id is not None:
				(status, user) = UserService().read(id)

				if status is False or user is None:
					return { 'status': False, 'message': 'User id [{}] is not valid'.format(id) }

			if state is not None:
				(status, state) = StateService().read(None, state)

				if status is False or state is None:
					return { 'status': False, 'message': 'State provided [{}] is not valid'.format(state) }

			if city is not None:
				(status, city) = CityService().read(None, city)

				if status is False or city is None:
					return { 'status': False, 'message': 'City provided [{}] is not valid'.format(city) }

			(status, visit) = VisitService().create(user.id, state.id, city.id)
			return { 'status': status,
					'message': 'Visit has been added.' if status else 'An error exists',
					'data': visit.to_json()}

		except Exception as x:
			return {'status': False, 'message': str(x)}

	def delete(self, id=None, visit_id=None):
		try:
			if id is None:
				return { 'status': False, 'message': 'User Id is required.' }

			if visit_id is None:
				return { 'status': False, 'message': 'Visit Id is required.' }

			(status, user) = UserService().read(id)
			if status is False:
				return { 'status': False, 'message': 'User Id {} is not valid.'.format(id) }

			(status, visits) = VisitService().read(visit_id)
			if status is True and len(visits) > 0:
				visit = visits[0]

				if visit.get('user_id') == id:
					(status, visit) = VisitService().delete(visit_id)
					return { 'status': status,
							'message': 'Visit has been deleted.' if status else 'An error exists',
							'data': visit.to_json() }
			else:
				return { 'status': False,
						'message': 'Visit Id {} does not correspond with User Id {}'.format(visit_id, id) }

		except Exception as x:
			return {'status': False, 'error': str(x)}


API_URL = 'https://maps.googleapis.com/maps/api/geocode/json?latlng={},{}&key={}'
API_KEY = 'AIzaSyD9ILBIhfJYuIzdE9b_ILal2IIvBEjEXL0'  # this is my temp google api key

class CityGeoResource(Resource):
	''' This fetches the geographical information using google maps API. '''

	def get(self, id=None):
		try:
			(status, city) = CityService().read(id=id)
			if status is False or city is None:
				return { 'status': False, 'message': 'City Id {} is not valid.'.format(id) }

			url      = API_URL.format(city.latitude, city.longitude, API_KEY)
			response = requests.get(url)
			json     = response.json()

			return {'status': status, 'data': json["results"]}

		except Exception as x:
			return {'status': False, 'message': str(x)}
