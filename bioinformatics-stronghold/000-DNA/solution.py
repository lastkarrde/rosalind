def nucleotide_count(seq: str) -> str:
    """
    Counts the nucleotides in a DNA sequence.
    """

    return '{} {} {} {}'.format(seq.count('A'),
                                seq.count('C'),
                                seq.count('G'),
                                seq.count('T'))


assert nucleotide_count('AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC') == '20 12 17 21'


with open('rosalind_dna.txt', 'r') as fh:

    sequence = fh.read()

    print(nucleotide_count(sequence))
