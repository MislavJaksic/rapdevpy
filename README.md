## Python Project Template

```
# Note: Install Python 3

# Note: install Poetry for Linux
$: curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

# Note: install Poetry for Windows
$: (Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python
# Note: do NOT update Poetry, it will break itself

$: python get-poetry.py --uninstall
```

```
# Note: `.toml` project name and package have no match (rapdevpy; rapdevpy)
$: poetry install  # install all dependencies
```

### dist

```
$: pip install dist/rapdevpy-0.0.1-py3-none.any.whl

$: rapdevpy
```

### docs

```
$: poetry shell
$: cd docs
# Note: review source/conf.py and source/index.rst
$: make html
# Note: see docs in docs/build/apidocs/index.html
```

### rapdevpy

```
$: poetry run python ./rapdevpy/runner.py
```

### tests

```
$: poetry run pytest --durations=0
```

```
$: poetry run pytest --cov=rapdevpy --cov-report=html tests
#: Note: see coverage report in htmlcov/index.html
```

### poetry.lock

Dependencies, Python version and the virtual environment are managed by `Poetry`.

```
$: poetry search Package-Name
$: poetry add Package-Name[==Package-Version]
```

### pyproject.toml

Define project entry point and metadata.  

### setup.cfg

Configure Python libraries.  

### Linters

```
$: poetry run black .
```

### Publish

```
$: poetry config pypi-token.pypi PyPI-API-Access-Token

$: poetry publish --build
```

```
https://pypi.org/project/rapdevpy/
```
