from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

def reverse_complement(sequence: str) -> str:
    """
    Creates the reverse complement of a RNA sequence
    """

    coding_dna = Seq(sequence, IUPAC.unambiguous_dna)

    return str(coding_dna.reverse_complement())


assert reverse_complement('AAAACCCGGT') == 'ACCGGGTTTT'


with open('rosalind_revc.txt', 'r') as fh:

    sequence = fh.read()

    print(reverse_complement(sequence))
