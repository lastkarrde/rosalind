from collections import OrderedDict


def naive_frequent_kmer(sequence: str, k: int) -> [str]:
    """
    A naive implementation to find the most frequent kmer in a sequence.
    :param sequence: input sequence
    :param k: length of kmer to find
    :return: a list of the most common kmers of size k
    """
    sequence_length = len(sequence)
    frequent_kmers = []
    kmer_count = {}

    # create our dictionary of kmers
    for i in range(0, sequence_length):

        if (i + k) < sequence_length:
            kmer = sequence[i:i+k]

            if kmer in kmer_count.keys():
                kmer_count[kmer] +=1
            else:
                kmer_count[kmer] = 1

    # order the values
    ordered_kmer_count = OrderedDict(sorted(kmer_count.items(), key=lambda x: x[1]))

    # get one of the most common kmers
    top_kmer, top_kmer_count = ordered_kmer_count.popitem()
    frequent_kmers.append(top_kmer)

    # walk through the remaining kmers until we run out of kmers of count
    next_kmer, next_kmer_count = ordered_kmer_count.popitem()

    while next_kmer_count == top_kmer_count:
        frequent_kmers.append(next_kmer)

        next_kmer, next_kmer_count = ordered_kmer_count.popitem()

    return frequent_kmers

test_case = naive_frequent_kmer("ACGTTGCATGTCGCATGATGCATGAGAGCT", 4)

assert len(test_case) == 2
assert 'CATG' in test_case
assert 'GCAT' in test_case
