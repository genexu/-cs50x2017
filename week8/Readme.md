# Week 8 Note
## Recap
simple review cs50 and intruduction python

## From C to Python
#### basic
```c
#include <stdio.h>

int main(void) {
  printf("hello, world\n");
}
```

```python
def main():
  print("hello, world")  
  
if __name__ == "__main__":
  main()
```

#### function
```c
printf("hello, world\n");
```
```python
print("hello, world")  
```

#### loop
```c
while (true) {
  ...
}
for (int i = 0; i < x; i++) {
  ...
}
```
```python
while True:
  ...
  
for i in range(50):
  ...
```
#### variables
```c
int
char
double
...
int i = 0;

```
```python
weak var
i = 0
```

#### boolean expression
same betewwn c and python
```
i < 50
x > y
...
```

#### condition
```c
if (x < y) {
  ...
}
else if (x > y) {
  ...
}
else {
  ...
}
```
```python
if x < y:
  ...
elif x > y:
  ...
else:
  ...
```
#### array
```c
argv[0]
```
```python
sys.argv[0]
```
note: python array operniation is more easier

## Interpreted Languages
without compile
```

~$ clang hello.c
~$ ./hello
```
```
~$ pyhton hello.py
```

## Porting to Python
```python
module
cs50.get_char()
cs50.get_int()
...
bool
float
int
str
...
complex
list
tuple
range
set
dict
...
```

## hello.py
```python
def main():
  print("hello, world");
if __name__ == "__main__":
  main()
```
```
~$ python hello.py
```

## string
```python
import cs50

s = cs50.get_string()
print("hello, {}".format(s))
```
```python
s = input("name: ")
print("hello, {}".format(s))
```
note: pyhton2 vs python3

## int.py
```python
i = input("int: ")
print("hello, {}".format(i))

```

## inprecistion.py
```python
print("{:.55f}".format(1/10))
```

## ints.py
```python
x = input("x: ")
y = input("y: ")

print("{} plus {} is {}".format(x, y, x + y))
print("{} monus {} is {}".format(x, y, x - y))
print("{} times {} is {}".format(x, y, x * y))
print("{} divided {} is {}".format(x, y, x / y))
print("{} divided {} (and flooward )is {}".format(x, y, x // y))
print("remainder of {} divided {} is {}".format(x, y, x % y))
```

## temperature.py
```python
import cs50
f = cs50.get_float()
c = 5/9 * (f - 32)
print("{:.1f}".format(c))
```

## logical.py
```python
import cs50
c = cs50.get_char()
if c == 'Y' or c == 'y':
  print('yes')
elif c == 'N' or c == 'n':
  print('no')
else:
  print('error')
```
## positive.py
```python
import cs50

def main():
  i = get_positive_int()
  print("{} is a positive imterget".format(i))

def get_positive_int():
  n = -1
  while n < 1:
    print("n is ", end="")
    n = cs50.get_int()
  return n

if __name__ == "__main__":
  main()
```
## cough.py
```pyhton
  def main():
    cough(3)
    snezze(3)
    
  def cough(n):
    print('cough',3)
  
  def snezze(n):
    print('achee',3)
   
  def say(word, n):
    for i in range(n):
      print(word)
      
  def __name__ == "__main__":
    main()
```

## strlen.py
```python
s - cs50.get_string()
print(len(s))
```

## ascii0.py
```python
for i in range(65, 65 + 26):
  print("{} is {}".format(chr(i), i))
```

## argv0.py
```python
import sys

if len(sys.argv) == 2:
  print("hello, {}".format(sys.argv[1]))
  print("hello " + sys.argv[1])
```

## argv1.py
```python
import sys
for i in range(len(sys.argv)):
  print(sys.argv[i])
```

## argv2.py
```python
import sys
for s in sys.argv:
  for c in s:
    print(c)
  print()
```

## exit.py
```python
import cs50
import sys

if len(sys.argv) != 2:
  print("missing command-line argument")
  exit(1)
  
print("hello, {}".format(sys.argv[1]))
exit(0)
```

## compare1.py
```python
import cs50

print(s1: ", end="")
s1 = cs50.get_string()

print(s2: ", end="")
s2 = cs50.get_string()

if s1 != None and s2 != None:
  print(s1 == s2)
```

Remind: In c, you compare char *s1 and char *s2 will be False, bcz you are compare two pointer

## copy1.py
```python
import cs50

print("s: ", end="")
s = cs50.get_string()
if s == None:
  exit(1)
  
t1 = s.capitalize()
  
print("s: {}".format(s))
print("t: {}".format(t))

exit(0)
```
Ref: https://stackoverflow.com/questions/352478/capitalize-a-string

## swap.py
Remind: In c, if you just pass char as argument to function, it was make a copy of arg

In python => by value || by ref ??
REF https://stackoverflow.com/questions/986006/how-do-i-pass-a-variable-by-reference

```python
x = 1
y = 2

print("x is {}".format(x))
print("y is {}".format(y))
print("Swapping...")
x, y = y, x
print(Swapped.)
print("x is {}".format(x))
print("y is {}".format(y))
```

## structs0.py
```python
import cs50
form student import Student

students = []
for i in range(3):
  print("name: ", end="")
  name = cs50.get_string()
  
  print("dorm: ", end="")
  name = cs50.get_string()
  
  students.append(Student(anme, dorm))
  
for student in students:
  print("{} is in {}".format(student.name, student.dorm))
```

## structs1.py
```python
// Name: sutdent.py

class Student:
  def __init__(self, name, dorm):
    self.name = name
    self.dorm = dorm
```

## student.py
```python
import csv

file = open("students.csv", w)
writer = csv.writer(file)
for student in students:
  writer.writerow((student.name, student.dorm))
file.close()
```

## Revisiting Speller
Talking about c spell checker

## dictionary.py
```python
class Dictionary:
  def __init__(self):
    self.words = set()

  def check(self, word):
    return word.lower() in self.words
    
  def load(seld, dictionary):
    file = open(dictionary, "r")
    for line in file:
      self.words.adds(line.rstrip("\n"))
    file.close()
    reutrn True

  def size(seld):
    reutrn len(self.words)
  
  def unload(self):
    return True
```

## Height-Level Benefits
more easier
more quick development
focus on implement
...

## Web-based Sofware
Simple intruduction dimimiclly web solfware

## MVC
![](https://github.com/genexu/cs50x2017/blob/master/week8/Screenshot-2016-fall-lectures-8-at-1h44m57s.png)

## serve.py
```python
form http.server import BaseHTTPRequestHandler, HTTPServer

# HTTPRequestHandler class
class HTTPServer_RequestHandler(BaseHTTPRequestHandler):

  def do_GET(self):
    self.send_response(200)
    
    self.sned_header("Content-type", "text/html")
    self.end_header()
    
    seld.wfile.write(bytes("hello, world", "utf8"))
    return

port = 8080
server_address = ("0.0.0.0", port)
httpd = HTTPServer(server_address, HTTPServer_RequestHandler)

httpd.serve_forever()
```

## Web Frameworks
Introduction Frameworks

## Flask
http://flask.pocoo.org/
```python
form flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)

@app.route("/")
def index():
  reutrn render_template(index.html)

@app.route("/register", mathods=["POST"])
def register():
  if request.form["name"] == "" or request.form["dorm"] == "":
    reutrn render_template(failure.html)
  reutrn render_template(success.html)
```

```
~$ flask run --host=0.0.0.0 --port=8080
```
talking about template language engine
My persenal lovely: Jinja2 http://jinja.pocoo.org/docs/2.9/

## Closing Remarks
That's Ending

## Outro
[Video]
