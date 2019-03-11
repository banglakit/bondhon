def from_unicode(s: str) -> str:
    if '০' <= s <= '৯':
        return chr(ord(s) - 2486)
    
    raise NotImplementedError