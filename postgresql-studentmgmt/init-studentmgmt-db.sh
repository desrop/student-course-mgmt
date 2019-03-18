#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
	CREATE USER studentmgmt PASSWORD 'chuckles';
	CREATE DATABASE studentmgmt;
	GRANT ALL PRIVILEGES ON DATABASE studentmgmt TO studentmgmt;
EOSQL

psql  -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "studentmgmt" -f ./ddl/studentmgmt-01-sequences.sql -f ./ddl/studentmgmt-02-tables.sql -f ./ddl/studentmgmt-03-indexes.sql
psql  -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "studentmgmt" -f ./data/insert-01-courses.sql -f ./data/insert-02-students.sql -f ./data/insert-03-enrollments.sql