# pykostal - a python based kostal bridge

[![PyPI version](https://badge.fury.io/py/pykostal.svg)](https://pypi.org/project/pykostal/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pykostal.svg)
[![PyPI - Status](https://img.shields.io/pypi/status/pykostal.svg)](https://pypi.org/project/pykostal/)

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

Initially run the following in your virtualenv:

```bash
python setup.py bdist_wheel
```

Everytime you update setup.py, run the following in your virtualenv:

```bash
pip install -e .
```

To install pykostal, along with the tools you need to develop and run tests, run the following in your virtualenv:

```bash
pip install -e .[dev]
```

## publishing

```bash
python setup.py bdist_wheel sdist
twine upload dist/*
```
