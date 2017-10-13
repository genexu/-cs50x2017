# Week 10 Note
## Recap
database CRUD
...

## JavaScript
run both on client and severside

## Frosh IMs
basic intruduction

## JavaScript Syntax
```javascript
function foo(bar, baz) {
  ...
}
```

```javascript
while (true) {
   ...
}
for (let i = 0; i < n; i++) {
  ...
}
for (var key in object) {
  ...
}
```

```javascript
var i;
let i;
const i;
```

```javascript
if (condition) {
  ...
} else if (condition) {
  ...
} else {
  ...
}
```

```javascript
let x = [1,2,3]
```

```javascript
let quote = {
  name: 'Netflix, Inc.',
  price: 123.30,
  symbol: 'NFLX',
}

```

Note: JSON

## Javascript Features
Document tree node
dynamic you web appreaction

Event
- click
- moudedown
- mouseup
- mouseover
- drag
- keypress
- load
- change
...

!!! anonymous functions !!!
!!! callback !!!
!!! Ajax !!!

## dom0.html
```html
<!DOCTYPE html>

<html>
  <head>
    <script>
      function greet() {
        alert('hello, ' + document.getElementById("name").value
      }
    </script>
    <title>dom0</title>
  </head>
  <body>
    <form id="name" placeholder="Name", type="text">
    <button type="submit" onClick="greet()">
  </body>
</html>
```


## dom1.html
```html
<!DOCTYPE html>

<html>
  <head>
    <title>dom1</title>
  </head>
  <body>
    <form id="name" placeholder="Name", type="text">
    <button type="submit" onClick="greet()">
    <script>
        document.getElementById("name").onsubmit = function {
        alert('hello, ' + document.getElementById("name").value
      }
    </script>
  </body>
</html>
```

## dom2.html
```html
<!DOCTYPE html>

<html>
  <head>
    <title>dom2</title>
    <script>
        // JQuery
        $(document).ready(function() {
          $('#demo').submit(function(event) {
            alert('hello, ' + $('#name').val)
            event.preventDefault()
          })
        })
    </script>
  </head>
  <body>
    <form id="name" placeholder="Name", type="text">
    <button type="submit" onClick="greet()">
  </body>
</html>
```

## form1.html
```javascript
  let form = document.getElementById('registration')
  form.onsubmit = () => {
    if (form.email.value = '') {
      alert('missing email')
      return false
    }
    ...
    return true
  }
```

## form2.html
other example with Bootstrap

## form3.html
https://github.com/1000hz/bootstrap-validator

## blink.html
```javascript
elem.style.visibility == 'visible'
...
elem.style.visibility == 'hidden'
...
window.setInterval(blink, 500)
```

## storage.html
```javascript
localStorge.setItem('item_name', value)
localStorge.getItem('item_name')
```

## geolocation.html
geo information

## Ajax
https://developer.mozilla.org/en-US/docs/AJAX/Getting_Started

## ajax0.html
```
function quote() {
  var url = 'quote?symbol=' + $('#symbol').val()
  $.getJSON(url, function(data) {
    alert(data)
  })
}
```

## ajax1.html
```html
<script src="script.js">
```
  
## ajax2.html
```javascript
$('#quote').html(...)
$('#symbol').val('')
```

Flask route quote

## map.html
https://developers.google.com/maps/documentation/javascript/tutorial

```javascript
map = new google,maps.Map(element), {
  center: {lat: 123, lng: 123},
  zoom: 4
})
var marker = new google.maps.Marker({
  map: map,
  position: {lat: 123, lng: 123}
})
...
```

## Bootstrap
http://getbootstrap.com/

## Javascript Image manipulation
https://github.com/wadefagen/SimpleImage
```
var im = new SimpleImage('#iamge')
var pixel = image.getRGB(x, y)
image.setRGB(x, y, pixel)
...
```

## Closing Thourghts
talking about JS
