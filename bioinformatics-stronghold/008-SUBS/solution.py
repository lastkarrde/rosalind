S = 'CATAAGCTAGAAGCTAGAAGCTAGAAGCTAGGACTAAAGCTAGGTTTTCGCTGAAGCTAGAAGCTAGAGAAGCTAGTTAAGCTAGTTGAAGCTAGCAAGCTAGAAGCTAGGAAGCTAGAAGCTAGTCTTAAGCTAGATAGATCCGTCGAAGCTAGAAGCTAGAGGTAAAGCTAGGCCAAGCTAGATAAGCTAGGAAAGCTAGAAGCTAGAAGCTAGCACGTATCTAGTCAAGCTAGACTTCCCTAAGCTAGTAAGACAAGCTAGAAGCTAGATCCATAAGCTAGAAGCTAGGCAAGCTAGAAGCTAGTATAAGCTAGGCGCCTGAAGCTAGCCTGCTAAGCTAGAAGCTAGTAAAAAGCTAGACTGTAAGAAGCTAGAGAAGCTAGAAGCTAGTTTACAAGCTAGCAAGCTAGTATGTGTAGTTTCAAGCTAGCCAAGCTAGCAAAGCTAGTAAAGCTAGAAGCTAGGCAAGCTAGTTAAGCTAGACATAAAGCTAGTTAAGCTAGTGAAGCTAGGCTCTTGCAAGCTAGACCAAGCTAGGGAAGCTAGCGGCAAGCTAGATTCAAGCTAGAAGCTAGTAGGAAGCTAGCGAGAAGCTAGGCGACTTGCAAGCTAGATAAGCTAGAAGCTAGTAAAGCTAGTAAGCTAGGAAGCTAGAATTACAAAGCTAGAAGCTAGCAAAGCTAGCTCTGCCGAAGCTAGAAGCTAGGATAAGCTAGAAGAAGCTAGGCATCCAGCGAAAGCTAGTGAAGCTAGAAGAAGCTAGGAAGCTAGAAGCTAGTCAAGCTAGAAGCTAGTTGATATAAGCTAGAAGCTAGAAGCTAGACGGTTTGCAGAAGCTAGCCAAGCTAGAAGCTAGAAGCTAGATCGTAAGCTAGCTGCTGAAGCTAG'
T = 'AAGCTAGAA'

def find_locations(haystack: str, needle: str) -> str:

    start_locations = []
    i = 0 #start looking at the start of the haystack

    try:

        while True:

            idx = haystack.index(needle, i) + 1

            start_locations.append(str(idx))
            i = idx

    except ValueError:
        return ' '.join(start_locations)


assert find_locations('GATATATGCATATACTT', 'ATAT') == '2 4 10'

print(find_locations(S, T))

