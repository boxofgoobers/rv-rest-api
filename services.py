
from models import Base, CityModel, StateModel, UserModel, VisitModel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql://:@localhost/test', echo=False)

# allow our db models (Base) to be accessible via the session
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)


class CityService(object):
	''' This is a CRUD service class for the City model.'''

	def __init__(self):
		self.session = DBSession()

	def read_all(self):
		try:
			data = [city.to_json() for city in self.session.query(CityModel).all()]
			return (True, data)

		except Exception as x:
			return (False, x)

	def read(self, id=None, name=None):
		try:
			city = self.session.query(CityModel).filter(
					(CityModel.id == id) |
					(CityModel.name == name)
				).first()
			return (True, city)

		except Exception as x:
			return (False, x)

	# def create(self, name, state_id, status, latitude, longitude):
	# 	try:
	# 		# insert new object
	# 		city = CityModel(name=name, state_id=state_id, status=status,
	# 			latitude=latitude, longitude=longitude)
	# 		self.session.add(city)
	# 		self.session.commit()

	# 		# refresh new object with DB state
	# 		self.session.refresh(city)
			
	# 		return (True, city)

	# 	except Exception as x:
	# 		return (False, x)

	# def update(self, id, name, state_id, status, latitude, longitude):
	# 	try:
	# 		city = self.session.query(CityModel).filter(CityModel.id == id).one()

	# 		if name is not None:
	# 			city.name = name
	# 		if state_id is not None:
	# 			city.state_id = state_id
	# 		if status is not None:
	# 			city.status = status
	# 		if latitude is not None:
	# 			city.latitude = latitude
	# 		if longitude is not None:
	# 			city.longitude = longitude
			
	# 		self.session.add(city)
	# 		self.session.commit()

	# 		# refresh new object with DB state
	# 		self.session.refresh(city)

	# 		return (True, city)
			
	# 	except Exception as x:
	# 		return (False, x)

	# def delete(self, id):
	# 	try:
	# 		city = self.session.query(CityModel).filter(CityModel.id == id).one()
	# 		self.session.delete(city)
	# 		self.session.commit()
	# 		return (True, city)

	# 	except Exception as x:
	# 		return (False, x)


class StateService(object):
	''' This is a CRUD service class for the State model.'''

	def __init__(self):
		self.session = DBSession()

	def read_all(self):
		try:
			data = [state.to_json() for state in self.session.query(StateModel).all()]
			return (True, data)

		except Exception as x:
			return (False, x)

	def read(self, id, name):
		try:
			state = self.session.query(StateModel).filter(
					(StateModel.id == id) |
					(StateModel.name == name) |
					(StateModel.abbreviation == name)
				).one()
			return (True, state)

		except Exception as x:
			return (False, x)

	# def create(self, name, abbreviation):
	# 	try:
	# 		# insert new object
	# 		state = StateModel(name=name, abbreviation=abbreviation)
	# 		self.session.add(state)
	# 		self.session.commit()

	# 		# refresh new object with DB state
	# 		self.session.refresh(state)
			
	# 		return (True, state)

	# 	except Exception as x:
	# 		return (False, x)

	# def update(self, id, name, abbreviation):
	# 	try:
	# 		state = self.session.query(StateModel).filter(StateModel.id == id).one()

	# 		if name is not None:
	# 			state.name = name
	# 		if abbreviation is not None:
	# 			state.abbreviation = abbreviation
			
	# 		self.session.add(state)
	# 		self.session.commit()

	# 		# refresh new object with DB state
	# 		self.session.refresh(state)

	# 		return (True, state)
			
	# 	except Exception as x:
	# 		return (False, x)

	# def delete(self, id):
	# 	try:
	# 		state = self.session.query(StateModel).filter(StateModel.id == id).one()
	# 		self.session.delete(state)
	# 		self.session.commit()
	# 		return (True, state)

	# 	except Exception as x:
	# 		return (False, x)


class StateCityService(object):
	def __init__(self):
		self.session = DBSession()

	def read(self, state):
		try:
			state  = self.session.query(StateModel).filter(
				(StateModel.name == state) |
				(StateModel.abbreviation == state)).one()
			cities = self.session.query(CityModel).filter(CityModel.state_id == state.id).all()
			data   = [city.to_json() for city in cities]
			return (True, data)

		except Exception as x:
			return (False, x)


class UserService(object):
	''' This is a CRUD service class for the User model.'''

	def __init__(self):
		self.session = DBSession()

	def read_all(self):
		try:
			data = [user.to_json() for user in self.session.query(UserModel).all()]
			return (True, data)

		except Exception as x:
			return (False, x)

	def read(self, id):
		try:
			user = self.session.query(UserModel).filter(UserModel.id == id).one()
			return (True, user)

		except Exception as x:
			return (False, x)

	def create(self, first_name, last_name):
		try:
			# insert new user object
			user = UserModel(first_name=first_name, last_name=last_name)
			self.session.add(user)
			self.session.commit()

			# refresh new user object with DB state
			self.session.refresh(user)
			
			return (True, user)

		except Exception as x:
			return (False, x)

	# def update(self, id, first_name, last_name):
	# 	try:
	# 			user = self.session.query(UserModel).filter(UserModel.id == id).one()

	# 			if first_name is not None:
	# 				user.first_name = first_name
	# 			if last_name is not None:
	# 				user.last_name = last_name
				
	# 			self.session.add(user)
	# 			self.session.commit()

	# 			# refresh new user object with DB state
	# 			self.session.refresh(user)

	# 			return (True, user)
			
	# 	except Exception as x:
	# 		return (False, x)

	# def delete(self, id):
	# 	try:
	# 		user = self.session.query(UserModel).filter(UserModel.id == id).one()
	# 		self.session.delete(user)
	# 		self.session.commit()
	# 		return (True, user)

	# 	except Exception as x:
	# 		return (False, x)


class VisitService(object):
	def __init__(self):
		self.session = DBSession()

	def read_all(self):
		try:
			visits = self.session.query(VisitModel).all()
			data = [visit.to_json() for visit in visits]
			return (True, data)

		except Exception as x:
			return (False, x)

	def read(self, user_id):
		try:
			visits = self.session.query(VisitModel).filter(
					(VisitModel.user_id == user_id)
				).all()
			data = [visit.to_json() for visit in visits]
			return (True, data)

		except Exception as x:
			return (False, x)

	def read_cities_visited(self, user_id):
		try:
			cities = (self.session.query(CityModel)
				.join(VisitModel)
				.filter(VisitModel.user_id == user_id)
				.order_by(CityModel.name)).all()
			data = [city.to_json() for city in cities]
			return (True, data)

		except Exception as x:
			return (False, x)

	def read_states_visited(self, user_id):
		try:
			states = (self.session.query(StateModel)
				.join(VisitModel)
				.filter(VisitModel.user_id == user_id)
				.order_by(StateModel.name)).all()
			data = [state.to_json() for state in states]
			return (True, data)

		except Exception as x:
			return (False, x)

	def create(self, user_id, state_id, city_id):
		try:
			visit = VisitModel(user_id=user_id, state_id=state_id, city_id=city_id)
			self.session.add(visit)
			self.session.commit()
			self.session.refresh(visit)
			
			return (True, visit)

		except Exception as x:
			return (False, x)


	def delete(self, id):
		try:
			visit = self.session.query(VisitModel).filter(VisitModel.id == id).one()
			self.session.delete(visit)
			self.session.commit()
			return (True, visit)

		except Exception as x:
			return (False, x)
