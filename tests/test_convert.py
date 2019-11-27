from unittest.mock import create_autospec

import pytest

import bondhon


def test_convert_no_exist():
    conv_map: bondhon.Conversions = (
        ('feluda', 'topshe', create_autospec(bondhon.bijoy_classic.from_unicode)),  # noqa: E501
    )
    with pytest.raises(ValueError):
        bondhon.convert('utf-8', 'bijoy', 'ফখা', conv_map=conv_map)


def test_convert_ok():
    mocked = create_autospec(bondhon.bijoy_classic.from_unicode, return_value='s')  # noqa: E501
    conv_map: bondhon.Conversions = (
        ('utf-8', 'bijoy', mocked),
    )
    assert bondhon.convert('utf-8', 'bijoy', 'ফখা', conv_map=conv_map) == 's'
    mocked.assert_called_once_with('ফখা')


@pytest.mark.parametrize('source,destination,sample_text', [
    ('bijoy', 'bijoy', 'xkcd'),
    ('utf-8', 'utf-8', 'আমি'),
    ('bornosoft', 'bornosoft', 'xkcd'),
])
def test_convert_source_destination_same(
        source: str, destination: str, sample_text: str):
    assert bondhon.convert(source, destination, sample_text) == sample_text


def test_convert_source_destination_same_invalid_encoding():
    with pytest.raises(ValueError):
        bondhon.convert('kgu', 'kgu', 'sample_text')
