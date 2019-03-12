from unittest.mock import create_autospec

import pytest

import bondhon


def test_convert_no_exist():
    conv_map: bondhon.Conversions = (
        ('feluda', 'topshe', create_autospec(bondhon.bijoy_classic.from_unicode)),
    )
    with pytest.raises(ValueError):
        bondhon.convert('utf-8', 'bijoy', 'ফখা', conv_map=conv_map)


def test_convert_ok():
    mocked = create_autospec(bondhon.bijoy_classic.from_unicode, return_value='s')
    conv_map: bondhon.Conversions = (
        ('utf-8', 'bijoy', mocked),
    )
    assert bondhon.convert('utf-8', 'bijoy', 'ফখা', conv_map=conv_map) == 's'
    mocked.assert_called_once_with('ফখা')
