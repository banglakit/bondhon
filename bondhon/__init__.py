from typing import Tuple, Callable, Iterable

from bondhon import bijoy_classic

Conversions = Iterable[Tuple[str, str, Callable[[str], str]]]

AVAILABLE_CONVERSIONS: Conversions = (
    ('utf-8', 'bijoy', bijoy_classic.from_unicode),
)


def _get_available_conversion_list(conv_map: Conversions):
    return ', '.join(['{} -> {}'.format(s, d) for s, d, _ in conv_map])


def convert(from_encoding: str, to_encoding: str, string: str,
            conv_map: Conversions = AVAILABLE_CONVERSIONS):
    """
    Convert Bengali Text from one encoding, to another.
    :param from_encoding: The encoding of the source text.
    :param to_encoding: The encoding of the target text.
    :param string: The string value to convert.
    :param conv_map: An iterable of available conversion functions.
    :return: `string` converted to `to_encoding`.
    """

    for source, destination, func in conv_map:
        if source == from_encoding and destination == to_encoding:
            return func(string)

    raise ValueError('Cannot convert {} -> {}. Available Conversions: {}'
                     .format(from_encoding,
                             to_encoding,
                             _get_available_conversion_list(conv_map)))
