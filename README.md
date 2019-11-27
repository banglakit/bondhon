# bondhon

[![Test Status](https://github.com/banglakit/bondhon/workflows/Bondhon%20Tests/badge.svg)](https://github.com/banglakit/bondhon/actions)

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
>>> import bondhon

>>> bondhon.convert('utf-8', 'bijoy', 'আমি বাংলায় গান গাই।')
'Avwg evsjvq Mvb MvB|'  # Output in Bijoy ASCII / Classic
```

## Development Status

Currently in active development. (From: Col 1, To: Row 1)

|           | Bijoy | Boishakhi | Bongshi | BornoSoft |        Unicode       |
|:---------:|:-----:|:---------:|:-------:|:---------:|:--------------------:|
|   Bijoy   |   -   |           |         |           |           ✔          |
| Boishakhi |       |     -     |         |           |      In Progress     |
|  Bongshi  |       |           |    -    |           |                      |
| BornoSoft |       |           |         |     -     |                      |
|  Unicode  |       |           |         |           |           -          |