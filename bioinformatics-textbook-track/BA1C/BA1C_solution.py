def reverse_complement(sequence: str) -> str:
    """
    Creates the reverse complement of a RNA sequence
    """
    reversed_sequence = sequence[::-1]

    return reversed_sequence.replace('A', 't')\
                            .replace('C', 'g')\
                            .replace('G', 'c')\
                            .replace('T', 'a')\
                            .upper()


assert reverse_complement('AAAACCCGGT') == 'ACCGGGTTTT'