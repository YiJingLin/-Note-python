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
threading.Thread()
```

- assign a task to the thread
```python
def task(target_name):
	print('complete the task:{}'.format(target_name))
new_thread = threading.Thread(target=task(target_name='taskA'))
```

- start the thread
```pytohn
new_thread = threading.Thread(target=task)
new_thread.start()
```