# pykostal - a python based kostal bridge

[![PyPI version](https://badge.fury.io/py/pykostal.svg)](https://pypi.org/project/pykostal/)
[![PyPI - Status](https://img.shields.io/pypi/status/pykostal.svg)](https://pypi.org/project/pykostal/)
[![Tests](https://github.com/DAMEK86/pykostal/actions/workflows/test.yml/badge.svg)](https://github.com/DAMEK86/pykostal/actions/workflows/test.yml)

**Python 3.9+ compatible** - Tested on Python 3.9, 3.10, 3.11, 3.12, and 3.13.

Python module for [Kostal](https://www.kostal-solar-electric.com/) piko inverters supporting:

- current-values
  - analog-inputs
  - battery
  - grid
  - home
  - pv-generator
  - s0-in
- home
- info.versions
- statistics
  - day
  - log-data
  - total

not supported:

- all settings
- events

ongoing:

- response code mapping (e.g. status code)

## Installation

Run the following to install:

```python
pip install pykostal
```

## Usage

```python
import kostal

# create instance
inverter = kostal.Piko(aiohttp.ClientSession(), url)
```

## Developing pykostal

### Prerequisites
- Python 3.9 or higher (tested up to Python 3.13)

### Initial setup
Run the following in your virtual environment:

```bash
python -m build
```

### Development installation
Every time you update the project, run the following in your virtual environment:

```bash
pip install -e .
```

To install pykostal along with the tools you need to develop and run tests, run the following in your virtual environment:

```bash
pip install -e '.[dev]'
```

### Running tests
```bash
pytest
```

### Testing across Python versions
```bash
tox
```

## Publishing

### Modern approach (recommended)
```bash
python -m build
twine upload dist/*
```

### Legacy approach
```bash
python setup.py bdist_wheel sdist
twine upload dist/*
```
