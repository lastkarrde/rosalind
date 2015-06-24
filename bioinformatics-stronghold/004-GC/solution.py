from Bio.Seq import Seq
from Bio import SeqIO
from Bio.Alphabet import IUPAC
from Bio.SeqUtils import GC


def calculate_gc_content(sequence: Seq) -> float:
    """
    Calcuates the percentage of GC within a sequence. Returns a float with 6DP.
    """

    gc_content = GC(sequence)

    return round(gc_content, 6)


assert calculate_gc_content(Seq('CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT',
                                IUPAC.unambiguous_dna)) == 60.919540

gc_content_dict = {}

for rec in SeqIO.parse('rosalind_gc.txt', 'fasta'):

    gc_content_dict[rec.id] = calculate_gc_content(rec.seq)


highest_gc_content = sorted(gc_content_dict.items(), key=lambda x: x[1])[-1]

print(highest_gc_content[0])
print(highest_gc_content[1])
