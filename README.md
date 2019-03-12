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
import bondhon

bondhon.convert('utf-8', 'bijoy', 'আমি বাংলায় গান গাই।')
```

## Development Status

Currently in active development.

|           | Bijoy | Boishakhi | Bongshi | BornoSoft |        Unicode       |
|:---------:|:-----:|:---------:|:-------:|:---------:|:--------------------:|
|   Bijoy   |   -   |           |         |           | In Progress, Working |
| Boishakhi |       |     -     |         |           |                      |
|  Bongshi  |       |           |    -    |           |                      |
| BornoSoft |       |           |         |     -     |                      |
|  Unicode  |       |           |         |           |           -          |