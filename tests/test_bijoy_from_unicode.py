import pytest

from bondhon import bijoy_classic


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
    assert bijoy_classic.from_unicode(given) == expected


@pytest.mark.parametrize('given,expected', [
    ('ং', 's'),
    ('ঃ', 't'),
    ('অ', 'A'),
    ('আ', 'Av'),
    ('ই', 'B'),
    ('ঈ', 'C'),
    ('উ', 'D'),
    ('ঊ', 'E'),
    ('ঋ', 'F'),
    ('এ', 'G'),
    ('ঐ', 'H'),
    ('ও', 'I'),
    ('ঔ', 'J'),
    ('ক', 'K'),
    ('খ', 'L'),
    ('গ', 'M'),
    ('ঘ', 'N'),
    ('ঙ', 'O'),
    ('চ', 'P'),
    ('ছ', 'Q'),
    ('জ', 'R'),
    ('ঝ', 'S'),
    ('ঞ', 'T'),
    ('ট', 'U'),
    ('ঠ', 'V'),
    ('ড', 'W'),
    ('ঢ', 'X'),
    ('ণ', 'Y'),
    ('ত', 'Z'),
    ('থ', '_'),
    ('দ', '`'),
    ('ধ', 'a'),
    ('ন', 'b'),
    ('প', 'c'),
    ('ফ', 'd'),
    ('ব', 'e'),
    ('ভ', 'f'),
    ('ম', 'g'),
    ('য', 'h'),
    ('র', 'i'),
    ('ল', 'j'),
    ('শ', 'k'),
    ('ষ', 'l'),
    ('স', 'm'),
    ('হ', 'n'),
    ('া', 'vw'),
    ('ি', 'w'),
    ('ী', 'x')
])
def test_individual_chars(given, expected):
    assert bijoy_classic.from_unicode(given) == expected