# bondhon

[![CircleCI](https://circleci.com/gh/banglakit/bondhon/tree/master.svg?style=svg)](https://circleci.com/gh/banglakit/bondhon/tree/master)

Encoding conversion library for the Bengali (বাংলা) script.

## Why does this exist?
A readable implementation for Python projects. Also, to serve as a
reference implementation for other languages.

## Installation

```
$ pip install git+https://github.com/banglakit/bondhon.git
```

## Basic Usage

```python
from bondhon import bijoy_classic

bijoy_classic.from_unicode('আমি বাংলায় গান গাই।')
```

## Development Status

Currently in active development.