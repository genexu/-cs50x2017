# Week 9 Note

## Week 8 Recap
- C and Python
- MVC
- Flask
```python 
from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def index():
  return render_template("index.html")
```

## froshims0
```
|_ template/
|_ application.py
```

```python
@app.route("/register", methods=["POST"])
request.form["name"]
```

```pyhton
{% extend "layout.html" %}

{% block title %}
...
{% endblock %}

{% block main %}
...
{% endblock %}
```

## froshims1
use csv storage data
```python
import csv
// a => append; w => write; r => read ...etc
file = open("register.csv", "a")
writer = csv.writer(file)
writer.writerow((request.form["name"], request.form["dorm"]))
file.close
```

## SQL
Structure Query System
- MSSQL
- MySQL
- MongoDB
...etc

Database
- table
- row and colume

Operation
- CREACT
- INSERT
- SELECT
- UPDATE
- DELETE
...

## phpLiteAdmin
SQLite
The Web-Based Database Management tool for SQLite  
https://www.phpliteadmin.org/

```
Field | Type | Primary Key | Autoincrease |  Not Null | Default Value
```
Type
- INTEGER
- REAL
- TEXT
- BLOB
- NUMERIC
- BOOLEAN
- DATETIME
...

### SQL Command
```sql
CREATE TABLE "table_name" ("field_name" Type [Option], ...)
```

```sql
INSERT INTO "table_name" ("field1", "field2") VALUES ("value1", ""value2)
```

```sql
SELECT * FROM "table_name" WHERE 1
```
```sql
UPDATE "table_name" SET "field_name" = "some value" WHERE "condition_filed" = "some value"
```

```sql
DELETE FOMR "table_name" WHERE "condition_field" = "some value"
``` 
Key Word: Unite Identify, Premary Key
Note: Premary Key will keep increase when use autoincrease

## SQL Built In
data
time
datetime
...

Primary key
Unique
Index
Not Null
Foreign Key
...

## Joining Tables 
!!! Database Normalization !!!

```sql
SELECT * FROM users 
JOIN zipcode 
ON users.zipcode = zipcode.id
```

REF http://www.dofactory.com/sql/join

## sqlite
```bash
~$ sqlite3 lecture.db
sqlite> .help
sqlite> .table
sqlite> .schema
aqlite> SELECT * FROM users;
```

## froshims2
```python
form cs50 import SQL
from flask import Flask, render_template_ redirect, request, url_for

app = Flask(__name__)

db = SQL("sqlite:///froshims2.db")

@app.route("/")
def index():
  reutrn render_template("index.html")
  
@app.route("/register", methods=["POST"])
def register():
  if request.form["name"] == "" or request.form["name"] == "":
    reutrn render_template("failure.html")
  db.execute("INSERT INTO registrants (name, dorm) VALUE(:name, :dorm)",
    name=request.form["name"], dorm=request.form["dorm"]) 
  return render_template("success.html")
    
@app.route("/registrants")
def registrants():
  rows = de.execute("SELECT * FORM registrants")
  render_template("registrants.html", registrants=rows)
  
@app.route("/unregister", methods=["GET", "POST"])
def unregister():
  if request.method == "GET"
    rows = db.execute("SELECT * FORM registrants")
    render_template("unregister.html", registrants=rows)
  elif request.method == "POST"
    if request.from["id"]:
      db.execute("DELETE FROM registrants WHERE id = :id", id=request.form["id"])
    return redurect(url_for("registrants"))
  
```

```html
<!-- Registrants -->
{% extends "layout.html" %}
  Registrants
{% block title %}

{% block main %}
  <ul>
    {% for registrant in registrants %}
      <li>{{ registrant.name }} from {{ registrant.dorm }}</li>
    {% endfor %}
  </ul>
{% endblock %}

{% endblock %}
```

```html
<!-- Unregister -->
{% extends "layout.html" %}
  Unregister
{% block title %}

{% block main %}
<form action="{{ url_for('unreigster') }} method="post"">
  <ul>
    {% for registrant in registrants %}
      <li>
         <input name="id" type="redio" vlaue={{ registrant.id }}>
        {{ registrant.name }} from {{ registrant.dorm }}
      </li>
    {% endfor %}
  </ul>
  <input type="submit" value="Unregister">
</from>
{% endblock %}

{% endblock %}
```

## ORM
SQLAlchemy
https://www.sqlalchemy.org/

## SQL Injection Attacks
![](https://github.com/genexu/cs50x2017/blob/master/week9/Screenshot-2016-fall-lectures-9-at-1h42m20s.png)
![](https://github.com/genexu/cs50x2017/blob/master/week9/Screenshot-2016-fall-lectures-9-at-1h44m10s.png)
![](https://github.com/genexu/cs50x2017/blob/master/week9/Screenshot-2016-fall-lectures-9-at-1h48m56s.png)
