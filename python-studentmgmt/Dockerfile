FROM python:3.6-alpine
RUN apk update
RUN apk add postgresql-dev gcc python3-dev musl-dev && pip3 install --no-cache-dir psycopg2 && pip3 install --no-cache-dir pipenv
WORKDIR /usr/src/app
COPY Pipfile Pipfile.lock bootstrap.sh ./
COPY studentmgmt ./studentmgmt
RUN pipenv install
EXPOSE 5000
CMD ./bootstrap.sh
