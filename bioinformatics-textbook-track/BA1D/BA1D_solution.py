def find_locations(haystack: str, needle: str) -> [int]:
    """
    Finds and returns all starting positions of the string needle in haystack.
    """

    start_locations = []
    i = 0

    # search until we're told we're at the end
    try:
        while True:

            idx = haystack.index(needle, i) + 1

            start_locations.append(idx - 1)
            i = idx

    except ValueError:
        return start_locations


assert find_locations('GATATATGCATATACTT', 'ATAT') == [1, 3, 9]
