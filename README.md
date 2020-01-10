# Ubuntu

# What is apache?

Apache is the most commonly used Web Server on Linux systems. Web servers are used to serve Web pages requested by client computers. Clients typically request and view Web pages using Web browser applications such as Firefox, Opera, Tor, Internet Explorer & Chrome.
so basically apache2 available in Ubuntu and in RHEL it's available by httpd.
 					We are introducing about apache2 here and How to install and launch web page in apache2.

## How to install apache2 in ubuntu.

- Process performed in `AWS Instance`. 
- First of all update ubuntu repo.

```console
$ apt update -y
```
- Install apache2 package.

```console
$ apt install apache2
```
- After installation check package version what it is.

```console
$ apache2 -version (or -v)
```
- Update in firewall(ufw known as) of ubuntu.
```console
$ ufw allow 'Apache'
```
- Check status of firewall.

```console
$ ufw status       #if it is inactive condition.

$ ufw enable       #make it enable.
```
- To service of apache2 make it start, stop, reload, restart etc. Take help of /etc/init.d/

```console
$ /etc/init.d/apache2 start/stop/restart/reload 

```










