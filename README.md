# Ubuntu # Apache2 # Web Server

# What is apache?

 Apache is the most commonly used Web Server on Linux systems. Web servers are used to serve Web pages requested by client computers. Clients typically request and view Web pages using Web browser applications such as Firefox, Opera, Tor, Internet Explorer & Chrome.
so basically apache2 available in Ubuntu and in RHEL it's available by name of httpd (package name).
			We are introducing about apache2 here and How to install and launch web page in apache2.

![logo](https://)

## How to install apache2 in ubuntu.

- Process performed in `AWS Instance`. 

- First of all update pre-installed packages.

```console
$ apt update -y
```
- Install apache2 package.

```console
$ apt install apache2
```
- After installation check package version what it is.

```console
$ apache2  -version (or -v)
```
- Update in firewall(known as ufw) of ubuntu.
```console
$ ufw allow 'Apache'
```
- Check status of firewall.

```console
`$ ufw status `     #if it is inactive condition.

`$ ufw enable `      #make it enable.
```
- To make it service start, stop, reload, restart of apache2. Take help of  `/etc/init.d/`

```console
$ /etc/init.d/apache2 start/stop/restart/reload 

```
- To check status of apache2 .
```console
$ systemctl status apache2
```
 Apache2 configuration uses scripts to manage modules and sites (vhosts). The scripts are below :-

- a2ensite
- a2dissite
- a2enmod
- a2dismod
- a2enconf
- a2disconf

 Overview of the directories & configuration files that are important :-

- `/var/www/html/ `   to publish web page of frontend.
- `/etc/apache2/apache2.conf ` to manage configuration settings of apache.
- `/etc/apache2/ports.conf `  to manage listening ports.
- `/etc/apache2/ sites-available`  to configure multiple virtual host sites.

 ### Host multiple sites on single server.

- By default, apache identifies the /var/www/html/ directory as the root directory of any web content we serve. 
- This one needs to be changed when hosting multiple domains on one server.

```console
$ mkdir /var/www/station30.com

$ mkdir /var/www/station31.com
```
- Make sure file permissions of directory will be according to sub directory.

```
We can set file permissions with help of  ```chmod 755 directory-name ```.
````
- Create index.html file in that hosting directory and also check file permissions.

```console
$ touch /var/www/station30.com/index.html

$ touch /var/www/station31.com/index.html 
```
- Default configuration path located in `/etc/apache2/sites-available/000-default.conf ` when serve content from one domain.

- To host more then one domain so we have to make a individual configuration file.

- /etc/apache2/sites-available/station30.com.conf
```console
$ <VirtualHost *:80>             
    ServerAdmin     admin@localhost (mail-address)
    ServerName      station30.com
    ServerAlias       www.station30.com   
    DocumentRoot  /var/www/station30.com/html/
    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```
- /etc/apache2/sites-available/station31.com.conf

```console
$ <VirtualHost *:80>             
    ServerAdmin     admin@localhost (mail-address)
    ServerName      station31.com
    ServerAlias       www.station31.com   
    DocumentRoot   /var/www/station31.com/html/
    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```
- After configuration, make it enable by command and each changes in configuration file restart the service of apache2.
 
```console
$ a2ensite station30.com.conf

$ a2ensite station31.com.conf

$ systemctl restart apache2
```
- After set new configuration file, disable it default configuration file and restart the service of apache2.

```console
$ a2dissite 000-default.conf

$ systemctl restart apache2
```






