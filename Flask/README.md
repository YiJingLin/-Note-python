# Flask
> Feb 10, 2018
## **outline**	
	- [get started](#get started)
	- [render](#render)
	- [router](#router)

<div id="get started"></div> 
## get started

```python
from flask import Flask
app = Flask(__name__)
```

<div id="render"></div> 
## [render](#)


### basic return

```python
@app.route("/")
def hello():
	return "Hello World!"
```

### with status

```python
@app.route("/")
def hello():
	return "Hello World!", 200
```

### render html

```python
@app.route("/")
def hello():
	return render_template('index.html', name=name)
```

### error handler

```python
@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404
```

<div id="router"></div> 
## [router](#)

```python
```
