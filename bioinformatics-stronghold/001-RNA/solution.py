def dna_to_rna(dna: str) -> str:
    """
    Converts a DNA sequence to equivilant RNA.
    """

    return dna.replace('T', 'U')


assert dna_to_rna('GATGGAACTTGACTACGTAAATT') == 'GAUGGAACUUGACUACGUAAAUU'

with open('rosalind_rna.txt', 'r') as fh:

    dna = fh.read()

    print(dna_to_rna(dna))
