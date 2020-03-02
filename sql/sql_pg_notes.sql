-- >> heroku login
-- >> heroku pg:info -a jobvizzy
-- >> heroku pg:psql


-- postgresql edt, need to run first in psql shell
-- dont forget semi colon at the end of stmt to exe 
CREATE TABLE "user" (
	"id"	BIGSERIAL NOT NULL PRIMARY KEY,
	"username"	VARCHAR(20) NOT NULL UNIQUE,
	"email"	VARCHAR(120) NOT NULL UNIQUE,
	"image_file"	VARCHAR(255) NOT NULL,
	"password"	VARCHAR(255) NOT NULL
)

-- psql THAT ACTUALLY WORKS
CREATE TABLE post (
	id BIGSERIAL NOT NULL PRIMARY KEY, 
	title VARCHAR(100) NOT NULL, 
	date_posted TIMESTAMP NOT NULL, 
	content TEXT NOT NULL, 
	user_id BIGINT NOT NULL REFERENCES public.user 
)

-- psql command execute with ; at the end
CREATE TABLE jobtitle (
	id BIGSERIAL NOT NULL PRIMARY KEY, 
	jobtitle VARCHAR(100) NOT NULL, 
	deleteprev VARCHAR(100) NOT NULL 
)


-- postgres
CREATE TABLE city (
	id BIGSERIAL NOT NULL PRIMARY KEY, 
	city VARCHAR(100) NOT NULL, 
	deleteprev VARCHAR(100) NOT NULL 
)

-- psql command execute with ; at the end
CREATE TABLE pair (
	id BIGSERIAL NOT NULL PRIMARY KEY, 
	jobtitle VARCHAR(100) NOT NULL, 
	city VARCHAR(100) NOT NULL, 
	deleteprev VARCHAR(100) NOT NULL 
)


-- psql command execute with ; at the end
-- create post table
CREATE TABLE post (
	id BIGSERIAL NOT NULL PRIMARY KEY, 
	title VARCHAR(100) NOT NULL, 
	date_posted TIMESTAMP NOT NULL, 
	content TEXT NOT NULL, 
	user_id BIGINT NOT NULL REFERENCES public.user 
)

-- Query all rows and columns from a table
SELECT * FROM
t

-- Delete the table from the database
DROP TABLE
t CASCADE

-- -- Remove all data in a table
TRUNCATE TABLE
t CASCADE

-- delete all records 
delete * from public.TABLE

ALTER TABLE public.user ALTER COLUMN user.password TYPE VARCHAR(255);
