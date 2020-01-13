FROM centos
RUN yum install httpd python36 -y
RUN pip3 install mysql-connector

COPY index.html /var/www/html/index.html

COPY python.py  /var/www/cgi-bin/python.py
RUN chmod +x /var/www/cgi-bin/python.py
ENV MYSQL_HOST $MYSQL_HOST
EXPOSE 80
ENTRYPOINT httpd -DFOREGROUND
