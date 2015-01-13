def reverse_complement(sequence: str) -> str:
    """
    Creates the reverse complement of a RNA sequence
    """

    reversed = sequence[::-1]
    reversed = reversed.replace('A', 't')
    reversed = reversed.replace('C', 'g')
    reversed = reversed.replace('G', 'c')
    reversed = reversed.replace('T', 'a')

    return reversed.upper()


assert reverse_complement('AAAACCCGGT') == 'ACCGGGTTTT'


with open('rosalind_revc.txt', 'r') as fh:

    sequence = fh.read()

    print(reverse_complement(sequence))
