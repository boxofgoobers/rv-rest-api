
START TRANSACTION;

DROP TABLE IF EXISTS test.user;
DROP TABLE IF EXISTS test.city;
DROP TABLE IF EXISTS test.state;

CREATE TABLE test.user (
	id              INTEGER     NOT NULL AUTO_INCREMENT,
	first_name      VARCHAR(50) NOT NULL,
	last_name       VARCHAR(50) NOT NULL,
	date_added      TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	date_time_added TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	last_updated    TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	PRIMARY KEY (id)
);


CREATE TABLE test.city (
	id           INTEGER     NOT NULL AUTO_INCREMENT,
	name         VARCHAR(50) NOT NULL,
	state_id     INTEGER     NOT NULL,
	status       VARCHAR(10) NOT NULL,
	latitude     DECIMAL(9, 6),
	longitude    DECIMAL(9, 6),
	date_added      TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	date_time_added TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	last_updated    TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	PRIMARY KEY (id)
);

CREATE TABLE test.state (
	id              INTEGER     NOT NULL,
	name            VARCHAR(50) NOT NULL,
	abbreviation    VARCHAR(10) NOT NULL,
	date_added      TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	date_time_added TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	last_updated    TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	PRIMARY KEY (id)
);

CREATE TABLE test.visit (
	id              INTEGER NOT NULL AUTO_INCREMENT,
	user_id         INTEGER NOT NULL,
	state_id        INTEGER NOT NULL,
	city_id         INTEGER NOT NULL,
	date_added      TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	date_time_added TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	last_updated    TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	PRIMARY KEY (id)
);

COMMIT;


START TRANSACTION;

LOAD DATA LOCAL INFILE 'data-user.csv'
	INTO TABLE user
	COLUMNS TERMINATED BY ','
	LINES TERMINATED BY '\n'
	IGNORE 1 LINES
	(first_name, last_name, date_added, date_time_added, last_updated)
;
LOAD DATA LOCAL INFILE 'data-city.csv'
	INTO TABLE city
	COLUMNS TERMINATED BY ','
	LINES TERMINATED BY '\r'
	IGNORE 1 LINES
	(name, state_id, status, latitude, longitude, date_added, date_time_added, last_updated)
;
LOAD DATA LOCAL INFILE 'data-state.csv'
	INTO TABLE state
	COLUMNS TERMINATED BY ','
	LINES TERMINATED BY '\n'
	IGNORE 1 LINES
	(id, name, abbreviation, date_added, date_time_added, last_updated)
;

COMMIT;

DESCRIBE user;
DESCRIBE city;
DESCRIBE state;

SELECT 'user'  AS 'Table', COUNT(*) AS 'Count' FROM user UNION
SELECT 'city'  AS 'Table', COUNT(*) AS 'Count' FROM city UNION
SELECT 'state' AS 'Table', COUNT(*) AS 'Count' FROM state;
