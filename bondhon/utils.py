import re

KARS_BEFORE_CHAR = ['ি', 'ে', 'ৈ']

SWAP_BEFORE_KARS = re.compile(
    r'(?P<char>[^{kars}])(?P<kar>[{kars}])'
    .format(kars=''.join(KARS_BEFORE_CHAR))
)


def swap_kar_location(s):
    return SWAP_BEFORE_KARS.sub('\\g<kar>\\g<char>', s)


FIX_UNICODE = [
    ('য়', 'য়'),
    ('ব়', 'র'),
    ('ঢ়', 'ঢ়'),
    ('ড়', 'ড়'),
]


def fix_unicode(s: str):
    for lookup, replacement in FIX_UNICODE:
        s = s.replace(lookup, replacement)

    return s
