# Flask
> Feb 10, 2018

## outline	
- [render](#render)
- [router](#router)

<div id="getstarted"></div> 

## get started

```python
from flask import Flask
app = Flask(__name__)
```

<div id="render"></div>

# [render](#)


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
from flask import render_template

@app.route("/")
def hello():
	return render_template('index.html', name=name)
```

### redirect

```python
from flask import redirect

@app.route("/")
def hello():
    return redirect('./redirect')
```

### error handler

```python
from flask import render_template

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404
```

<div id="router"></div>

# [router](#)

### public folder (static)

```python
# all files are public under 'static' folder
app_pub = Flask(__name__, static_folder='static', static_url_path='/static/')

```
