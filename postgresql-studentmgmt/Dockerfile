FROM postgres:11
WORKDIR /docker-entrypoint-initdb.d
COPY init-studentmgmt-db.sh ./
COPY ddl ./ddl
COPY data ./data