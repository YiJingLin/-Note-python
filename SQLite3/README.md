# SQLite
> Feb 11, 2018

## get started

```python
import sqlite3
```

### db connection

```python
db = sqlite3.connect('./db/test.db')
```

### execute sql query

```python
query = 'select * from table'
db.execute(query)
```

### execute sql file

```python
sql_file_path = './create_db.sql'
with open(sql_file_path) as f:
    create_db_sql = f.read()

with db:
    db.executescript(create_db_sql)
```

### store back to db and close db connection

```python
db.commit()
db.close()
```