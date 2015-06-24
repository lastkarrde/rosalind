from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

def dna_to_rna(dna: str) -> str:
    """
    Converts a DNA sequence to equivilant RNA.
    """

    coding_dna = Seq(dna, IUPAC.unambiguous_dna)


    return str(coding_dna.transcribe())


assert dna_to_rna('GATGGAACTTGACTACGTAAATT') == 'GAUGGAACUUGACUACGUAAAUU'

with open('rosalind_rna.txt', 'r') as fh:

    dna = fh.read()

    print(dna_to_rna(dna))
