# isbnlib-worldcat
A metadata extension for the isbnlib Python library that pulls information from the WorldCat database (https://worldcat.org/).

## Requirements
Requires the following Python modules:
* isbnlib (version >= 3.9.1)
* pycountry (version >= 1.12.8)
* beautifulsoup4 (version >= 4.7.1)

These are all available from PyPI (https://pypi.org/).

## Installation
#### 1. Using pip

```shell
pip install isbnlib-worldcat2
```
Pip will automatically take care of all required dependencies.

#### 2. Manually using setup.py

First, make sure that you have installed the required dependencies. Then you can clone the git repository and build the module using setup.py.
```shell
git clone https://github.com/pwssnk/isbnlib-worldcat
cd isbnlib-worldcat/
python setup.py install
```

## Usage
Once installed, a new metadata provider for isbnlib named 'worldcat' will be available.

```python
import isbnlib

isbnlib.meta(isbn='9781509304523', service='worldcat')
```

## License
(c) 2019 pwssnk -- Code available under LGPL v3 license
