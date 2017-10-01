# Week 6 Note
## Week 5 Recap
- linked list
- stack => push pop
- queue => enqueue dequeue
- binary search tree
- hufman tree
- hash table
- tries

## web programing
![](https://github.com/genexu/cs50x2017/blob/master/week6/Screenshot-2016-fall-lectures-6-at-6m19s.png)

## Warriors of the Net Teaser
[Video]

## Home Networking
![](https://github.com/genexu/cs50x2017/blob/master/week6/Screenshot-2016-fall-lectures-6-at-8m53s.png)

## DHCP & IP
Dynamic Host Configuration Protocol (DHCP)
IP <=> IP
ipv4
#.#.#.#

Private IPs
10.#.#.#
172.16.#.# - 172.31.#.#
192.168.#.#

## IPs in the Media
[Video]

## DNS
Domain Name Sysytem
IP => Domain Name

## Routers
route information
decide which way data should go

## nslookup
```
~$ nslookup www.google.com
```
## traceroute
```
~$ traceroute -q 1 www.google.com
```
## Undersea Cobling
[Video]
Here are all og the Udersea Cables
That Power The Interne 

## Packets
packet info between me and target

## TCP/UDP
slice data pack and sead <=> repack the seed
check <=> chack

## Port
21 FTP
22 SSH
25 SMTP
53 DNS
80 HTTP
443 HTTPS

## Firewall
keep packet out or in
block ip and port

## VPN
Visual Private Network

## Warriors of the Net
https://www.youtube.com/watch?v=PBWhzz_Gn10
[Video]

## HTTP
Intrucduction Http

## GET
Get request
GET/ HTTP/1.1
Host: www.harvard.edu
...

response
HTTP/1.1 200 OK
Content-Type: text/html

## Status Codes
- 200 OK
- 300 Moved Permanently
- 302 Founf
- 304 Not MOdified
- 401 Unauthorized
- 403 Forbudden
- 404 Not Found
- 500 Internal Server Error
...

## telent
```
~$ telnet www.harvard.edu 80 > output.txt
GET / HTTP/1.1
Host: www.harvard.edu
[Enter]
[Enter]
~$ more output.txt
```

## curl
```
~$ curl -I http://www.harvard.edu/
```
301 Moved Permanently
HTTPS - cant another know what you see between you and server

## Query Strings
https://google.com/search?q=cat

## HTML
![](https://github.com/genexu/cs50x2017/blob/master/week6/Screenshot-2016-fall-lectures-6-at-1h16m29s.png)

## hello.html
```html
<!DOCTYPE html>

<html>
  <head>
    <title>hello, world<title>
  </head>
  <body>
    hello, world
  </body>
</html>
```

## iamge.html
```html
<img src="" alt="" />
```

## link.html
```html
<a href="">Link</a>
```
## parapraphs.html
```html
<p>say some thing</p>
```
```
<head>
  <meta name="viewport" content="width=devoce-width, initial-scale=1 ">
</head>
```

## headings.html
```html
<h1>One</h1>
<h2>Two</h2>
<h3>Three</h3>
<h4>Four</h4>
<h5>Five</h5>
<h6>Six</h6>
```

## list.hmtl
```hmtl
<ul> // <ol>
  <li>One</li>
  <li>Two</li>
  <li>Three</li>
</ul>
```

## table.html
```html
<table>
  <tr>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</table>
```

## css0.html
```css
font-size
font-weight
text-align
...
```

## css1.hmtl
```css
#id {
}
.class {
}
```

## css2.html
```html
<link href="cssfile.css" rel="stylesheet">
```
Note: spiciel char

## POST
request
POST /login.php HTTP/1.1
Host: www.facebook.com
...
email=useranme@example.om&pass=123456

```html
<form action="https://www.google.com/search" method="get">
  <input name="q" type="text" />
  <input type="submit" />
</form>
```

## Outor
[Video]
