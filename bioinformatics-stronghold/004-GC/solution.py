def calculate_gc_content(sequence: str) -> float:
    """
    Calcuates the percentage of GC within a sequence. Returns a float with 6DP.
    """

    gc_content = sequence.count('G') + sequence.count('C')
    percentage = (gc_content * 100) / float(len(sequence))

    return round(percentage, 6)


assert calculate_gc_content('CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT') == 60.919540


highest_gc_label = '-1'
highest_gc_content = -1


with open('rosalind_gc.txt', 'r') as fh:

    curr_header = ''
    curr_seq = ''
    curr_gc_content = float

    for line in fh:

        if line[0] == '>':


            # the first time we encounter a header, we have no sequence so we need this check
            if curr_seq != '':

                curr_gc_content = calculate_gc_content(curr_seq)

                #print('Curr: {} - {}'.format(curr_header, curr_gc_content))

                if curr_gc_content > highest_gc_content:
                    highest_gc_label = curr_header
                    highest_gc_content = curr_gc_content

            curr_header = line[1::].strip()
            curr_seq = ''
            curr_gc_content = -1

        else:
            curr_seq += line.strip()



    curr_gc_content = calculate_gc_content(curr_seq)

    #print('Curr: {} - {}'.format(curr_header, curr_gc_content))

    if curr_gc_content > highest_gc_content:
        highest_gc_label = curr_header
        highest_gc_content = curr_gc_content


print(highest_gc_label)
print(highest_gc_content)
