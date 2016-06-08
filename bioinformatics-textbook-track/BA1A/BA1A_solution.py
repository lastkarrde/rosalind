def pattern_count(text: str, pattern: str) -> int:
    """
    Count the occurances of pattern in text
    """
    text_length = len(text)
    pattern_length = len(pattern)
    count = 0
    i = 0

    while i < (text_length - pattern_length + 1):

        if text[i:i+pattern_length] == pattern:
            count += 1

        i += 1

    return count

