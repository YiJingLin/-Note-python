# BeautifulSoup
> Feb 04, 2018

## Get started

### Installation

```shell
pip install beautifulsoup4
```

### import ur package

```python
from bs4 import BeautifulSoup
from urllib.request import urlopen
```

### load html wth bs4

```python
url = "https://morvanzhou.github.io/"
html = urlopen(url).read().decode('utf-8')
soup = bs(html, features='lxml')
soup
```

## useful functions

### [**find all**](#)

### find_all(<tag_nm>)

```python
tag_nm = "a"
\\\\
a_tags = soup.find_all(tag_nm)
```

### find_all() with attr. filter

```python
tag_nm = "a"
a_table_tags = soup.find_all(tag_nm, {"class":"table"})
```

### find_all() with regular expression filter

```python
import re
tag_nm = "a"
a_jpg_tags = soup.find_all(tag_nm, {"class":re.compile('.*?\.jpg')})
```

### [get content](#)

### get_text

```python
a_tag = soup.find('a')
a_tag.get_text()
```

### get attribute value

```python
a_tag = soup.find('a')
a_tag['href']
```