from Bio import SeqIO

def create_adjacency_list(file_name: str, k: int):
    """
    Create an adjacency list of sequences from file_name with
    overlap of length k.
    """

    sequences = {}
    adjacency_map = {}

    # establish our sequences
    for rec in SeqIO.parse(file_name, 'fasta'):
        sequences[rec.id] = str(rec.seq)
        adjacency_map[rec.id] = []

    # for each of our sequences...
    for key in sequences.keys():

        # check this sequence against all other sequences..
        other_seqs = list(sequences.keys())
        other_seqs.remove(key)

        this_suffix = sequences[key][-k:]

        # do the actual comparison
        for other_key in other_seqs:
            if this_suffix == sequences[other_key][:k]:
                adjacency_map[key].append(other_key)

    # now format it..
    for key, val in adjacency_map.items():
        if val:
            for seq in val:
                print('{} {}'.format(key, seq))

create_adjacency_list('challenge_inputs.fasta', 3)