# Threading
> Jan 29, 2018

## get started
```python
import threading
```

## threading infomation

- threads count
```python
threading.active_count()
```

- list threads 
```python
threading.enumerate()
```

- current thread
```python
threading.current_thread()
```

## create a thread
- create new thread
```python
new_thread = threading.Thread()
```

- thread naming
```python
thread_name = 'threadA'
threading.Thread(name=thread_name)
```

- assign a task to the thread
```python
def task():
	...

new_thread = threading.Thread(target=task)
```

- assign a task with arguments to the thread
```python
def task(name, score):
	...

new_thread = threading.Thread(target=task, args=(name,score))
```

## thread process
- start the thread
```pytohn
new_thread.start()
```

- join the thread
```pytohn
new_thread.join()
```

- thread lock
```pytohn
lock.acquire()
...
lock.release()
```
