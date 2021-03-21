## Rapid Development Library for Python

```
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

TODO: how to use the library insutrction

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
