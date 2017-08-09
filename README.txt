Code project to build a small RESTful API using Python / Flask / MySQL.

# install python 3 (I used version 3.6.2)
# install pip      (I used version 9.0.1)
# install mysql    (I used version 10.1.25-MariaDB)

$ cd <install-directory>/rv-rest-api

# MySQL - create schemas and load data
#
# the default 'test' database will be used
# populate the database with table schemas and data

$ cd rv_data
$ mysql -h localhost test < database_schema-mysql.sql


# Python PIP - install package dependencies
#
# flask           - web framework
# flask-restful   - support for building RESTful APIs
# mysqlclient     - interface to the MySQL database
# SQLAlchemy      - database SQL tookit and ORM mapper

$ cd ..
$ pip list
$ sudo pip install flask
$ sudo pip install flask-restful
$ sudo pip install mysqlclient
$ sudo pip install SQLAlchemy
$ pip list

# launch application
#
$ python main.py
