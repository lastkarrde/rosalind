from Bio import motifs, SeqIO


def create_consensus_table(filename: str) -> str:
    """
    Generates the consensus table & string from sequences from a fasta file.

    We can't just call m.counts directly, it displays column headers and floats which
    rosalind doesn't want.
    """

    counts = {}

    input_sequences = [rec.seq for rec in SeqIO.parse(filename, 'fasta')]

    m = motifs.create(input_sequences)

    for row in list(m.counts.items()):
        counts[row[0]] = [str(x) for x in row[1]]  # need strings to do the ' '.join

    # m.counts displays column headers and floats. rosalind doesn't want this..

    return "{}\n{}\n{}\n{}\n{}".format(m.consensus,
                                       'A: ' + ' '.join(counts['A']),
                                       'C: ' + ' '.join(counts['C']),
                                       'G: ' + ' '.join(counts['G']),
                                       'T: ' + ' '.join(counts['T']))


assert create_consensus_table('sample_inputs.fasta') == '''ATGCAACT
A: 5 1 0 0 5 5 0 0
C: 0 0 1 4 2 0 6 1
G: 1 1 6 3 0 1 0 0
T: 1 5 0 0 0 1 1 6'''

print(create_consensus_table('challenge_inputs.fasta'))