import pytest

from bondhon import boishakhi


@pytest.mark.parametrize('given,expected', [
    ('১', '1'),
    ('২', '2'),
    ('৩', '3'),
    ('৪', '4'),
    ('৫', '5'),
    ('৬', '6'),
    ('৭', '7'),
    ('৮', '8'),
    ('৯', '9'),
    ('০', '0'),
])
def test_numbers(given, expected):
    assert boishakhi.from_unicode(given) == expected


@pytest.mark.parametrize('given,expected', [
    ('আমি বাংলায় গান গাই', 'Awxi gwvlwt Mwd MwB')
])
def test_alpha_sentence(given, expected):
    assert boishakhi.from_unicode(given) == expected
