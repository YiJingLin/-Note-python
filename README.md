# -Note-python
Note for python toolkit

[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)

## Update :

### [pyTorch - Dataset and Dataloader](#)
> Apr 27, 2018
([link](./pyTorch/3-5%20utils.Data.ipynb)), ([ref](https://morvanzhou.github.io/tutorials/machine-learning/torch/3-05-train-on-batch/))
- __Data.TensorDataset(data_tensor=x, target_tensor=y)__
- __Data.DataLoader(dataset = torch_dataset, batch_size, shuffle, n_workers)__

### [pyTorch - Tensor advanced function](#)
> Apr 27, 2018
([link](./pyTorch/2-1%20Tensor%20advanced%20functions.ipynb)), ([ref](https://www.zhihu.com/question/60321866))
- __Tensor.is_contiguous()__ _(boolean)_ : check if tensor is contiguous or not
- __Tensor.contiguous()__ _(none)_ : return contiguous tensor

### [pyTorch - Tensor functions](#)
> Apr 26, 2018
([link](./pyTorch/1-1%20Tensor%20functions.ipynb)), ([ref](http://pytorch.org/docs/stable/torch.html))
- __view__ : like numpy reshape
- __squeeze__ : remove redundant dimension
- __unsqueeze__ : add new one-dim to specified index (dimension).


### [Matplotlib - ColorMap](https://matplotlib.org/tutorials/colors/colormaps.html)
> Apr 09, 2018

### [SQLite3](https://docs.python.org/2/library/sqlite3.html)
> Feb 11, 2018
- db = sqlite3.connect(filepath)
- db.execute(query)

### Flask :
> Feb 10, 2018
- app = Flask(__name__)
- render
- router

### Crawler/Requests :
> Feb 09, 2018
- requests.get
- requests.post
	- data
	- cookies
	- files
- requests.Session()

### Crawler/BeautifulSoup :
> Feb 04, 2018
- find_all
	- attribute filter
	- regular expression
- get content
	- result.get_text()
	- result[<attr>]

### map, filter and reduce :
> Feb 03, 2018

- **map** : map(func, list)
- **filter** : filter(func, list)
- **reduce** : reduce(func, list)
(you should import reduce in functools)

### Threading :
> Jan 29, 2018

- **new thread** : threading.Thread()
- **join** : Thread().join
- **lock** : threading.Lock()

### Numpy.random :

> Jan 26, 2018

- random_smaple
- random_rand
- **random_choice**

### Tkinter: 

> Dec 28 - 07, 2017

- Window and button
- input
- radio button and scroll bar
- check button
- **Canvas**
- Menu bar