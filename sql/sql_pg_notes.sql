-- Query all rows and columns from a table
SELECT * FROM
t

-- Delete the table from the database
DROP TABLE
t CASCADE

-- -- Remove all data in a table
TRUNCATE TABLE
t CASCADE


-- delete * from public.

-- psql
CREATE TABLE post (
	id BIGSERIAL NOT NULL PRIMARY KEY, 
	title VARCHAR(100) NOT NULL, 
	date_posted TIMESTAMP NOT NULL, 
	content TEXT NOT NULL, 
	user_id BIGINT NOT NULL REFERENCES public.user 
)

-- sql
CREATE TABLE post (
	id INTEGER NOT NULL, 
	title VARCHAR(100) NOT NULL, 
	date_posted DATETIME NOT NULL, 
	content TEXT NOT NULL, 
	user_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(user_id) REFERENCES user (id)
)
-- psql
CREATE TABLE "proday" (
	"id"	BIGSERIAL NOT NULL PRIMARY KEY,
	"title"	VARCHAR(100),
	"desc"	VARCHAR(100),
	"date_posted"	TIMESTAMP,
	"cat01"	VARCHAR(100),
	"act01"	VARCHAR(100),
	"done01"	BOOLEAN,
	"cat02"	VARCHAR(100),
	"act02"	VARCHAR(100),
	"done02"	BOOLEAN,
	"act03"	VARCHAR(100),
	"cat03"	VARCHAR(100),
	"done03"	BOOLEAN,
	"cat04"	VARCHAR(100),
	"act04"	VARCHAR(100),
	"done04"	BOOLEAN,
	"icon01"	VARCHAR(100),
	"icon02"	VARCHAR(100),
	"icon03"	VARCHAR(100),
	"icon04"	VARCHAR(100),
	"count_c01"	SMALLINT,
	"count_c02"	SMALLINT,
	"count_c03"	SMALLINT,
	"count_c04"	SMALLINT,
	"countD_c01"	SMALLINT,
	"countD_c02"	SMALLINT,
	"countD_c03"	SMALLINT,
	"countD_c04"	SMALLINT,
	"count_done"	SMALLINT,
	"count_total"	SMALLINT,
	"perc_done"	SMALLINT,
	"message_total"	VARCHAR(256),
    "user_id"	BIGINT REFERENCES public.user
)

-- SQLITE
CREATE TABLE "proday" (
	"id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"title"	VARCHAR(100),
	"desc"	VARCHAR(100),
	"date_posted"	DATETIME,
	"user_id"	VARCHAR(100),
	"cat01"	VARCHAR(100),
	"act01"	VARCHAR(100),
	"done01"	REAL,
	"cat02"	VARCHAR(100),
	"act02"	VARCHAR(100),
	"done02"	REAL,
	"act03"	VARCHAR(100),
	"cat03"	VARCHAR(100),
	"done03"	REAL,
	"cat04"	VARCHAR(100),
	"act04"	VARCHAR(100),
	"done04"	REAL,
	"icon01"	VARCHAR(100),
	"icon02"	VARCHAR(100),
	"icon03"	VARCHAR(100),
	"icon04"	VARCHAR(100),
	"count_c01"	INTEGER,
	"count_c02"	INTEGER,
	"count_c03"	INTEGER,
	"count_c04"	INTEGER,
	"countD_c01"	INTEGER,
	"countD_c02"	INTEGER,
	"countD_c03"	INTEGER,
	"countD_c04"	INTEGER,
	"count_done"	INTEGER,
	"count_total"	INTEGER,
	"perc_done"	INTEGER,
	"message_total"	VARCHAR(256)
)

-- postgres
CREATE TABLE "task" (
	"id"	BIGSERIAL NOT NULL PRIMARY KEY,
	"title"	VARCHAR(32) NOT NULL,
	"content"	TEXT,
	"done"	BOOLEAN,
	"is_urgent"	TEXT,
	"is_important"	TEXT,
	"matrix_zone"	TEXT,
	"border_style"	TEXT,
	"urg_points"	SMALLINT,
	"imp_points"	SMALLINT,
	"date_posted"	TIMESTAMP,
	"user_id"	BIGINT REFERENCES public.user
)
-- sqlite
CREATE TABLE "task" (
	"id"	INTEGER NOT NULL,
	"title"	INTEGER,
	"content"	NUMERIC,
	"done"	REAL,
	"is_urgent"	TEXT,
	"is_important"	TEXT,
	"matrix_zone"	TEXT,
	"border_style"	TEXT,
	"urg_points"	INTEGER,
	"imp_points"	INTEGER,
	"date_posted"	DATETIME,
	"user_id"	INTEGER,
	PRIMARY KEY("id")
)

-- postgresql edt, need to run first in psql shell

	CREATE TABLE "user" (
		"id"	BIGSERIAL NOT NULL PRIMARY KEY,
		"username"	VARCHAR(20) NOT NULL UNIQUE,
		"email"	VARCHAR(120) NOT NULL UNIQUE,
		"image_file"	VARCHAR(255) NOT NULL,
		"password"	VARCHAR(255) NOT NULL);


-- SQLITE
CREATE TABLE "user" (
	"id"	INTEGER NOT NULL,
	"username"	VARCHAR(20) NOT NULL UNIQUE,
	"email"	VARCHAR(120) NOT NULL UNIQUE,
	"image_file"	VARCHAR(20) NOT NULL,
	"password"	VARCHAR(120) NOT NULL,
	"imp_pts"	INTEGER,
	"urg_pts"	INTEGER,
	"total_pts"	INTEGER,
	"imp_perc"	INTEGER,
	"urg_perc"	INTEGER,
	"avatar_img"	BLOB,
	"avatar_mode"	TEXT,
	PRIMARY KEY("id")
)

ALTER TABLE public.user ALTER COLUMN user.password TYPE VARCHAR(255);


-- psql command that actually works
CREATE TABLE post (
	id INTEGER NOT NULL PRIMARY KEY, 
	title VARCHAR(100) NOT NULL, 
	date_posted TIMESTAMP NOT NULL, 
	content TEXT NOT NULL, 
	user_id INTEGER NOT NULL REFERENCES user, 
)

-- sqlite browser copy create statement
CREATE TABLE post (
	id INTEGER NOT NULL, 
	title VARCHAR(100) NOT NULL, 
	date_posted DATETIME NOT NULL, 
	content TEXT NOT NULL, 
	user_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(user_id) REFERENCES user (id)
)


