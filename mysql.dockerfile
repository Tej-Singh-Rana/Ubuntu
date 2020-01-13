FROM mysql
ENV MYSQL_DATABASE users

COPY ./script /docker-entrypoint-initdb.d/
