import datetime
from sqlalchemy import create_engine, Column, Date, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.dialects.mysql import TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation, relationship

Base = declarative_base()

class CityModel(Base):
	__tablename__   = 'city'

	id              = Column(Integer, primary_key=True)
	name            = Column(String(50), nullable=False)
	state_id        = Column(Integer,    nullable=False)
	status          = Column(String(10), nullable=False)
	latitude        = Column(Float,     nullable=False)
	longitude       = Column(Float,     nullable=False)
	date_added      = Column(TIMESTAMP, nullable=False)
	date_time_added = Column(TIMESTAMP, nullable=False)
	last_updated    = Column(TIMESTAMP, nullable=False)

	def to_json(self):
		return model_to_json(self)


class StateModel(Base):
	__tablename__   = 'state'

	id              = Column(Integer, primary_key=True)
	name            = Column(String(50), nullable=False)
	abbreviation    = Column(String(3), nullable=False)
	date_added      = Column(TIMESTAMP, nullable=False)
	date_time_added = Column(TIMESTAMP, nullable=False)
	last_updated    = Column(TIMESTAMP, nullable=False)

	def to_json(self):
		return model_to_json(self)


class UserModel(Base):
	__tablename__   = 'user'

	id              = Column(Integer, primary_key=True)
	first_name      = Column(String(50), nullable=False)
	last_name       = Column(String(50), nullable=False)
	date_added      = Column(TIMESTAMP, nullable=False)
	date_time_added = Column(TIMESTAMP, nullable=False)
	last_updated    = Column(TIMESTAMP, nullable=False)

	def to_json(self):
		return model_to_json(self)


class VisitModel(Base):
	__tablename__   = 'visit'

	id              = Column(Integer, primary_key=True)
	user_id         = Column(Integer, ForeignKey("user.id"),  nullable=False)
	state_id        = Column(Integer, ForeignKey("state.id"), nullable=False)
	city_id         = Column(Integer, ForeignKey("city.id"),  nullable=False)
	date_added      = Column(TIMESTAMP, nullable=False)
	date_time_added = Column(TIMESTAMP, nullable=False)
	last_updated    = Column(TIMESTAMP, nullable=False)

	user  = relationship("UserModel",  foreign_keys='VisitModel.user_id')
	state = relationship("StateModel", foreign_keys='VisitModel.state_id')
	city  = relationship("CityModel",  foreign_keys='VisitModel.city_id')

	def to_json(self):
		return model_to_json(self)


def model_to_json(object):
	# return dir(self)

	# return {p: self.__dict__[p] for p in dir(self)
	# 	if not (p.startswith('_')
	# 		| p.startswith('__')
	# 		| p.startswith('metadata') ) and not callable(getattr(self, p))}

	# return {key: getattr(self, key) for key in self.__mapper__.c.keys() }

	data = {}
	for key in object.__mapper__.c.keys():
		value = getattr(object, key)

		# if isinstance(value, datetime.datetime):
		# 	value = str(value)
		# elif isinstance(value, decimal.Decimal):
		# 	value = str(value)
		# else:
		# 	value = str(value)

		data[key] = str(value)
	return data
