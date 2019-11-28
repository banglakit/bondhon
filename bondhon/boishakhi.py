from .utils import fix_unicode
from .utils import swap_kar_location

__all__ = ['from_unicode']


CHAR_TABLE = {
    2437: 'A',
    2438: 'Aw',
    2439: 'B',
    2440: 'C',
    2441: 'D',
    2442: 'E',
    2443: 'F',
    2447: 'G',
    2448: 'H',
    2451: 'I',
    2452: 'J',
    2453: 'K',
    2454: 'L',
    2455: 'M',
    2456: 'N',
    2457: 'O',
    2458: 'P',
    2459: 'Q',
    2460: 'R',
    2461: 'S',
    2462: 'T',
    2463: 'U',
    2464: 'V',
    2465: 'W',
    2466: 'X',
    2467: 'Y',
    2468: 'Z',
    2469: 'a',
    2470: 'b',
    2471: 'c',
    2472: 'd',
    2474: 'e',
    2475: 'f',
    2476: 'g',
    2477: 'h',
    2478: 'i',
    2479: 'j',
    2480: 'k',
    2482: 'l',
    2486: 'm',
    2487: 'n',
    2488: 'o',
    2489: 'p',
    2524: 'r',
    2525: 's',
    2527: 't',
    2510: 'u',
    2434: 'v',
    2494: 'w',
    2495: 'x',
    2496: 'y',
    2509: 'z',
    2534: '0',
    2535: '1',
    2536: '2',
    2537: '3',
    2538: '4',
    2539: '5',
    2540: '6',
    2541: '7',
    2542: '8',
    2543: '9'
}

# TODO: Add khiyo transformation


def from_unicode(s: str) -> str:
    s = fix_unicode(s)
    # s = replace_conj(s)
    s = swap_kar_location(s)
    # s = handle_surrounding_char(s)

    s = s.translate(CHAR_TABLE)

    return s
