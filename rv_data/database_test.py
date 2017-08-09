from data_models import Base, User #City, State, User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# generate a db instance
engine = create_engine('mysql://:@localhost/test', echo=False)

# allow our db model objects to be accessible via the session
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)


def Main():


	# generate a db session 
	session = DBSession()

	# userBalonie = User(first_name='Balonie', last_name='Mahonie')
	# session.add(userBalonie)
	# session.commit()

	# ---------------------------------------------
	# using sessions, query returns model Objects
	# ---------------------------------------------

	# users = session.query(User).filter(User.last_name == 'Smith').all()
	for user in session.query(User).all():
		print(user.to_json())
		# print( dict(zip(user.__dict__.keys(), user.__dict__.values())) )

	# for city in session.query(City).all():
	# 	print('{}: {}'.format(city.rowid, city.name))

	# for state in session.query(State).all():
	# 	print('{}: {}, {}'.format(state.rowid, state.abbreviation, state.name))


	# ---------------------------------------------
	# using connections, query returns tuple Objects
	# ---------------------------------------------
	# connection = engine.connect()
	# rs = connection.execute("SELECT * FROM user")
	# for user in rs:
	# 	print(user)
		# print( dict(zip(user.keys(), user.values())) )
		# print('{}: {} {}'.format(user.id, user.first_name, user.last_name))

	# print( rs.keys() )
	# for row in rs:
	# 	print( row )
	# rs = connection.execute("SELECT * FROM city")
	# for row in rs:
	# 	print( row )
	# rs = connection.execute("SELECT * FROM state")
	# for row in rs:
	# 	print( row )
	# connection.close()



if __name__ == '__main__':
	Main()