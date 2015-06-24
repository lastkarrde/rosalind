from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

def assemble_protein(rna: str) -> str:
    """
    Translate an RNA string into it's protein string.
    """

    coding_rna = Seq(rna, IUPAC.unambiguous_rna)

    return coding_rna.translate(to_stop=True)


assert assemble_protein('AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA') == 'MAMAPRTEINSTRING'

print(assemble_protein('AUGAUAUUAACCUCCAUAAACAGGUUACCCGCCGGAAGUAGUACCACCGACCUCGAUGGACUGUCGCCUAUUGUCGACUGCCUCCAUCGCAGCGAACUUCUAGGUUCUCGCGAUACUGAAAGUACUCAGACAUGUGGGGGUCACAAGUUAAGUUGGCUCCACGUUGACCCAGUGGACAUUGUUCCCUGUACCCAUAGUCGGACUCCUAAUAUGGUUUUGGCCGGGCGGGACUGUAAGAAACCAAAAUUCACUGUAAACUAUCCCGAUCAUCGCAUAGGUCCUCAUUGUAUACCUAUUCCACCGGAUGGGGAUGGAGCCCAAAACACAGGCUGCAUAAAGGGGCAUACUUUGUCUCACACUGGCAAUAUACACGAGGACUCGACAUUUUGCUGCUUUCCGUUGUUCGUUGACCAGUCAAGUGGGGAGGAAGAAUUCCAUAGUUCUCAAAUGAGGAUUUCAAAGGCCACGUGGCCCAGAGUCAACAACGAGACCGCUGACGACUCUUCCUGCCCUCUUGUGGUCGCUACAGCUGCCGGCAUUCAUACCAGCGUUUCCGCUCAGGGUUCGAAAGGCGUUAGCCGCUCAACAAAGACUUUCAUGAAGGUUUGUGUCAUGCAUGCAACUGAGACGCUGCAGCGACGGGCAGGGUCUUGGGACGCAACCGAUGUUAUGCCGGGCCAACCAUUGAAUGUAGUACGCUGGGUAGUGAAAGUUAGAACAGAAGUUGAACAUGUGCUAGACUGCCUGAUUAUUACCGACGCUUAUAGUACAUAUCUUAACGGACCAAGGGCGUGUGUUCCCUCACGUGAUUAUAUCCACUGCACAUAUAGGCUGUUUGCUAUUAUUCAGGCAGGUGGUGAUGUAAUUCAUCGAGCUCUUCUAUGUGCUUUGGGGCGUAUGUUACCCAUCCCCAGGGAGGGCGCCUUACUUCAAAUUUGGUAUGAAUACCUGGAACCUACUCUGUUGCAUGCGUGCGAGGGAACGAGCGUCCCCCUAGUUGGAGCUGCAUGCGAUGGUGCCAGUACAGUUAGAGUAUGCUGGGGUUGUGCCACCCUAAGACUGCACUCGAAGUCCUUCAGGGGCGCACUGUCCGUUGAUAAGGCCUCAUGGAGCAGGAAGUGCGACGGACCUUCUAGAAACGUGAAGGCGGUGUCGAACUUACGUGGUCGGGGCCAUAUGCGAGGCAGGAUUGAGUUGAUUAGCGAACUGGCGACGUGUUUACGCCAGGAUGAACGAGAGUGUCUUACGCUUUGGAUGGGUGUAUAUCUAUCACUCGUAUUCUACUCGGACGGAGUUGCGUGGAUCGCCUUAUCCAUGGUAUCCAGGGCAAUAAAAGCUUGGAAUUUUCCUUGUCGUGCUGGCCACUCAUGUGAAUGCAUAGGUCGAGGUGUCGGUGCAAAACGGGGAAACAUAGAGUCCGGCACACAGGGCUCUCAAACACCGUAUGGAGUCGCGGUGAAUGGAGUUGUCAAAGACAUCAGUUACUGUUGGGUAAAGCUACCCACAAAUAAACUGCCACGCCCGAGCGCGGACCUUGAAAGUGCGACGUGCUGCUGGAUCAAUCACCAGAGAGUCUUUUUAGGGCAGAUACAUUCGGGGUACGGAGGACUAGACGCGCACUUUACUGUACCGACUGGCGCCGUUAAUCGACGGCUGCCCUCUGAACGGCGACUAUUGUGGCCUCGAAGAACUGUGUUUGAGAAUAAAGCUUUUACUAAACACACACGCCUAUUCAAGGCGCCUCCGAAGGGAGCACUAAUAGAAUGCACCAGACGCCGAUGGCGCACUAGAGUGUGGCGAGUCACGAGGGUAUGUCCAUCGCACUCCGCCAUACAUUGCGGGUCGCGCCGGAUGCCGGCCCGCACCCUAAUCAUGUCCAGCAUCCAAUAUCCGUCAGGCUUUGCGAAGUAUUACAGGUGGUGGUCCAUGGGUAACGUUGAUACCUUGAGAUAUUAUUGCCCAGAAGGCCUUCUGAAUCAAAUGCUAAUGCCGACAGAACCGCGAUGUUCUUAUUCCCUUCCUCUAAUAGAAGACACACCACAGAUGGACUCAAGAUGUCUAGGCUCAGCCCCGGUGGAAAUAUGGGGUAGAAUAACUUCCCUAAACGUGCCUCGCCAGACUGAACUCUCUACCGUAAAUAACUUAUACACGCUAGCCUAUGCCCAACGUCGGCCGGGCUCUUCUGCGGUCUUAACUCUGCUGAGCGGACCUCACAUCCGGUACUAUUCCACGCCCGAUAUAAACCGAUCAGCCGUUAGUAGAGGAACUCGCGGUACGAUAAUAUCAGACCUUCUAGAAGUAUUCAUUCCCUACAAUGCCCCUCGUUGUAAAGGGCGUGAUGGGAGCUCUCUGGCGUAUCUCUGGAUGGUCAAGGUCCUGUUGAGACCAAGUCAUCCUACGGUUUUGAUCUUAAAGUUAAAUUUGCUCCGGGGCCUAUCCGUUAAUGAUCGGACACGUAGGGAGUAUCGUCGAACUUUCUUACGCGGAGUACGAGGCUGCGGUUAUCCGGCUCUCACGACUCAUCGACUUGGACUUUCGUGGUGUCAGGCAUCCAGUUCCGAGAUAUCUAUUCUUUUGACAUCGCGCUAUCUCGCCAACAGUCUCUUCACAAAUACUGGUAGGGACUACGACAAUAGUGAGCUGGGGGAUGCUUAUUCAAAGCACAGAUAUCUAUGUGUAGCGAGUGCAUUCGUCUCCGGGCCUAGGGGGGGCGAACCCAUAAACCGAAUCAUAUCUCUCGCUGCGGAAGGCACGUCUCUUAAGUUGCGUUCAGGCGCACGUGGAAUCAGAAGCUCCAGGCCCUGUGAUCUAGCGUUCUGUGGGCAGGGAAAAGCGAAACUUAAGCAAUUUAUAUCCGUACUCAACGAUUGCGGCUUUAACAAACGAAAGAGGCGGGUGAUGAUCCUUUUAGUGCUUGAUCACGAUACCGGCGGAUCUUGGUGGUACCGGGCGCCGAAAUUUCCCACGGUACUUUUAACGGAGGGAUCGCCCGUGCCAGGGGAAAGCCCAUCUGUAAAUUUUCCCGAGGUACGAUGUCUACGACAACGUAACCGUGGAGAGAAGUAUGGCGAAUAUCUACGACCGUGGCCGCGGGUUCUGAGACCAUGGAUAGCGAGUAUUGUUAUACUUUUCAUUGCUAGACAGACUAGGCUGCCCGGUUGUCGCAUCUUACCGAUAGACUUAGGCGAGGUAAUAAGUUGUUGCGAUGAGGGUUUCACAGCUCAACUCGCAAACUCAGUGGUCUUUUCGAGGUUAAUGACUCUCUCAAUAAUCAAAGCUGCUGAAAGACCGGGUGGCCAUAAGAAGGACGCCAUCAUGAAGAUCAAUGAUACUCAUAAUCGCAUCACUCCUAUUCUGUCGCGCUUAGUCAGGCAUCCGUUUGUAGCUUCCAGCGCACCGUGGCUGUUUGCUCCGAUUGAUUUACAGCGAAUUGAAGACACAACUCACAUUAUACCGGCAGUCCACAACAAGAGUGUUAUCAAUCAGGCUGUCAGCGUGCAGUAUCAGCUUCUGCAAUCAGGUAGAUUGCCGUGGCCCAGCGCCGCUCGUUUUGGGUCGACAUGCGUCGUGGCGCCAUACUUUGUUAUUGUGGGCGCUAAAGUGACUCCCGACUUAGACCCGCUCACGUGGUAUGUGUGUGACCCGGGCAAAUCAGACUCAUCGGGGGCAGUUAGAAUACACACAUUAACUGCACCACCGAGAGCUUACCUUCUGUCCCGCAUCGGAUUAGGCGGCCCCCGGAUAAAAGAUACCCCGGGGAGACAGACACACUGGGGUCUACGGCACAUCGGUACCACCGUACGUCGAAUGGGCGAGCGAUGUGACGGCGAAGGAAUCGUGGCCCUUAGGGUAGAGAGAAAAACAUUAGCCCGGAAUGAGGCCGGUACCUGUACGUGUUCCAUGGUGCAACAUGUCGGGGAGCUGCUAAGGCGCGCCGAGUGGGGAAAGACCCCAACAUUUGCAGACCUGAUGCGUGCUCUUUCGAUUGCCCAACGCAGCGGUUGCUCUCGCCGACCUUUGUCGCCUUUCUAUGCAAAACUAACUAUACGAUCGGCAAAAGUGGUUUACCAGGUUGAAUGUAUUUCCAUUACGUUGGAAAAGUCUCAAAUCGUAGGAGAAUCCAGCUUAGCUUCAGUGCAUCCUGGUCGCAUGGAAUUUCAAUGGUUCGCAGACAGUUCACAUUCUCCAUCUUUUCUAAUCCGGCGCGUCCAUGUAGUAAGCGCCACUAUGUGGUCUAUCAGAUCAGCCACUCAGCUUGUUUUUACCUCAGGUGAGACCUUCGGUGCAAGCUUACCAGCAGUUGUUCUCACUCCGGGAAGUUACGUACAUCUGGCGUUCGAUUGGGUUAGACGCACCAUCCCAGAUCCCAAAGCGGUGGAAAUCACGUCAACAUCUGGCAGGGGAAGCGUCUCCUGUAGCCAAUGUCUGAGUUUAGCCGGCGUUGUAAGCAGCCAGGGUCGCUUCCCUCACAGUAGGGGGCUCAGUCGGUGCCUGGCUCGUGAUGUUAACGAUAAGCGACGGAGUCCGCUGACAAGCAUACAUAUCACUUUCUUCCGGCAAGCCAACCGACAUUCGUGUCGAUUCGAUAUAAACCGGAUAACUGAUCGGUACGCCCGCCGGUCGCAGGAGUUUGUAAGCGAGUCCGCUAAGGAAACGCUAGGUACCACUGCUUCACAUACGUACUACAUCGCGCAACACCUUGCUACGGAUUGGAUUAUCUCCCCAGCAUGUGCAAUGGGUCCUUCCUUCUCGCAACCAUGUAUAACGCUGACUUCUCCAGGCUUCCCAAUGCCGGGGCACAAAAUACGAAUUCCACUAUAUGAUAUAAGGACAAGGUGGGUUCGGAGCGUUCUUGACAGAUACACAGUUGCCAACCCACCAUUCAUAGCCGAAUGCCGUCAUUGGAUACGGGAGCACCAUCUACUAAAUGGCCGCUGGGGCAACAGAACAUGGUUCAAACAUAGUAGCGAGCUCACCAUUUCGAGACAUACUGAGAUGCUAUGCAGAGCUCUGUAUCGGGGUAUGUUAAAUCCUGCCGGAGUGCGGGUUAGAAUGCAUGUGAUCACAAUAGAACCUAGGUACCUUGAAACGAAUGAUCUGCUGGCGCAGCUGCUUAACAGUGGAGGUAUGUCGCGCCACGGAGGGCCAACGCGGAUUUCAAUCCAGGACCACUGCUUGCUAUUAUUGAAACGUGCGACCCUCGAUGAGAUCGAGUACUCCCUCUCCAAGUUGUACUCUCGGGCGAUAGGGAUACUCAGGUCAAAUGGGCACUCCACACUGUCAGCGAAUUGGGAGCUAAACCUACUGGGCGAACGCAGGAAUCUCUUCUCAGUAAACCACGGAAAGGGUGCCGGGCUAGGUACGUUAUUGGAGCCUCUUACCUGCGUCCAACUUUUAGUGCUCGGGCGUGGCCCUGAAUGUCUGCCAAAAGUCGUAAAGACUGUGAUGUUGGGUAAACUAAAGCCGUGUUCUCCUAAUGAAUCGUGCCCUCGAGAUUUCUGGAGAGGUUACACGCCCCCGUGCACGUUUAGACUUAACAGCUGCAGUGGUUCGGGUGGUUCCAAAGCCCCAGGCGGUAGCCAGACUCAAGAUAGUGGGUCACAUGAGUUCCAACCUAUGUUACCUAUACAUCCGGUGUGGAUUUUUCAUACCAUCUAUCUUCCGCAUGUCCGUAAAGCGGAAGCGAAAACUGCCACAAACAUAUUAUCAGUACCAUCUGGAUGGGUGGGUGAGAUCGCUUUGCAAGAUAAAAUUCUCCGGUGUACGCGCUCUGUCUACGUGCGUAAACUGCGAACACACGCAGUCUCUCACCCGAUUCGAAGGAUACAAAGGAACACGUUGUUUAUGCGCGUGCGGAUAGGACCGAAUGCCGUCCAAACGCAGAACAGCUCUACAUCCCGCCGGCUGGAGUUGCGAACAGGACAAAGCGCACAGAAUCUAACCAGCCGAGGCGCCCGGCACUUUCUCGGCACUCAGUUCGCAAUCAAGGCGGGGGGCUCAAUGAGAUUGUUGUUCCUGAACUCAACUUCAACUGAGCGUAAGUGGAACUCCUAUAUAAAUUACAAUUUACAACUAACCACUGUAGUACCAUCUAAAUGGGCCUGGACUUCCCUUCUCCUCAGUCGGAGCCGAACCGUAGCAGAAGAACCUCCUUAUCUAAACGUGGGAUCGGGUCGGUCAAUUCUAAAACGCCCGGAUCUUUUGGCCAUCCCGUGUAUUGGUAGCUGUUCCUCCGGGGGGGUCAUCACCAUAGUACUAGAUGGGGGGAAGGUCAUUAGGCGGUGCUUCGUGCAUACCGACCCUAUGCAAUAUACCAUAACAGUCAACCUCCGAUGGUGUGACGCAUUGCAUCCAUGGGCCAUUUCCACCCCAUUUGUUCGGUGGGAUGUUUAUUUCUUGCUACGAAUCCGUUGGUGGAAGCAAAUACGGUUGGAGCCUCGAUCCCAGCUUCCUGAUAAUCGAACUAACCGCAGCAAAUAUAGCGGGUAUAUGUCUGGAAACUGUGGAACAAUGCGGGAUCGAGUGUAUUCGCUAUUGCGAGGCGUGAUACCAAUUACUGUGCAUAAUCAUCAGACAUUCGACCUUGGCCGCGAGGACUGUAGAGCAACGCUUUCACAACGGUUUCCUACCAGUGUUGGCAUAGCUGCACUAAAUGGAUCGGUUAGAGGCGGCCCCUUGACCCCUUCCGGAAGACGCAUAUGUGAAUGCAUGGUACCACAGUUUACGCACAACUUAGUUGUAUUUACCCUCACAGGUGACGGUAAAGAACAGUCGCCUCCUGGAGUAGGGCAACUACCAACGGCCUACCCUAACCGCUAUCGGGAAAAGAUAACAUUAAUAAAAGACUUUUGCGCUUUGGAUCCGAUUGUAUCAUCGUGCGCCCAUCUUCGACAGCAGGAACUUUUCUACUUCCCCUGCAUCUGCAUCAGACGUCUCUUAAAUGGGACAUCACUAUCAGCACGUCAAGCCUACUGCUGGCCAUUGAUCCUUCGCCUCGGCAGAGGCGAUAGGUCGCUACGAUGCGCGUGCAUAGGUCAAAGUCACGACCUGGUGUCCCUAAUUACUUUGCAGCCCUAUCGACCAAUACAUUACGCGAGUGUGCGCCUGUUGCGUCUAAAACACCAACUGCUUAGUGUCUUCACCCAAUGGGUCCGCCGGGUGGAGGAUACACCCGCCUCCCAAUGGGUAGCAACCUCAAUAGUAAAGCCCGUAGCUGUGAUCCUCCGGUUCCGACGCCCUUUGGAGGGCUUACAGGCUCCGAGUACCAUGCGCGAUAUCGGAGGUACCGUCAGGUCAAAGGAUGUCGAACUGGCACAUCCGGGGGCCACUCCCACUAAUGAGGUCAGUCCGCCCCUACUAAUCGGGCACAGUGUACCGGGCUCUCUACAUUUCUGCAACGGGGAGUCAACCGCAUUCAGUGCUACCACCCUACGCAACGUGUAUGGCCGACAUCUCAUCGUAUGCUCGUCAUGUUCCCCAAGUUAUCGACCAUACAAGCAUGUAGGCCACACCGUGGAUAACCUAAUUGAUCGUACGCUACUACUCUUCAGCUGGGUGAAGUAUUCAAAGAGUAGGGUGUCCUAUAACCAGGAUGCCGUUCCUCCUCAUCUACUAGGAGUUAUUAUAUGGAAUAGAGCCACUAUAGUUGCGAGCACCCGUGGGGAUAACAGUCGAGCCACUUUUACUUCGUCUAUUCCGAAGAAAUGGCUUCUCGACUUCCCGAGGUAUCGUGCAAAACAAAAAACUGCCAACUUGUGCCCUCUAGGUGGUGUCGAUCCCCCGUAUCUCACAGACUGGGGCGUCGACGGGAUCUAUACUAAUUAUGCAGGAGCCGGCGUACUACCAAGAUUGCGCCCCGGCCAUGCCCCUAACAGACUAGCCGCAUGUUGGUGUCGCAAGGAAGAGACUCUGCGCGAGUACGCUCCGUCCAAACGAAAGUCUUGUGUGGACCAUGUAGGUCUUCCGUUAUUAGACCCCGGACUUAAUUGUAUUCAAAUGGCACCGAUGGUGCUGUCCCGUUUCGACAUCUGCCCGUGUACCUCCUUGGAGGAAGAAGAGGAUAAGGACCUGAGAUACGGCAGGAUAUUUAAACCUGUAGCCUUGGAACAACUGUUCACGAAUAGUGUCUGUGUUUACAACUGUCCGGGUGGCAGAUUGGUCUACCCUCCGCCCAGGUUCUACAUGGACGGCAAAUCUUUUUCGAGUCUACCAGAAGGGCAUUUCAGGCCAUUCUGUGCCCCUAGAUGUCAAACCCUGUCAGGAGUCAUCUCGCUGGCGAAAAUGAACCUGCGCGUAGGUGCCGACCAACGGUGGUUACUCCGCGGGCAUAGGCUAAAUCUCCGGAUUAUUGGUUGCCGCCGGUUAGAUUUAGUUCUCUCACAAAGGGCUGGCGUGAUCCUUGUAGUAGACGCUACAGCCCCGGUAUUCAUGGAGAUUCUUCUAAAAGCCCUGUUUUGGCUGUUUGUUGUCGCUGACGGGGUUUACCGCUCGCCGGCCCGAGGUCUAGUUGUGAGCAUAGUUGCAUCCUUUGUGGCGCGGGUAGGAUCGCUGCUUUCUUACGACUACGAUCCGAUCUUCCGUUGUAGCGUGAUCGAGUUCGCUGCUUUAACUCCCCCGCCGCUUAGACGAGGGCAUUUCAUGACCAAUAUCCCAUGUACCGAAUGGAAGAUAUUCUUCAUGACCCACCAGGGACUCAGAAGCCUCGCCGGCCGUCGCGAAGAUCAGCGUAUCGGUCCUAUGGCCGUUAAGUUACUGUCAAAUUGGUAUGGCUACCAUGCCUGCCAUGCGACAGGUGUCUUACGCCCGGUAGUAGCUGGCUUGUUAGUGUGGGGGCCAGCGUUUACGUGUUCCCCAACGACUGUCGGUGUAUCCCCAAACUACUAUAUGCUAGUAUUGAUCGAUCGCGUCAUCACCACGACUUCAGCUUCGCCCGACGCGCGGGGCCUAAACCAACGGCCGCCAAAGUCACAAGGUGUAUUUCGAGGUAUUCUCGUGGCACCAAAUGGCGCGGAGUGUGGGCGGUACAGAUUAAGGUCUGGUUGUCUGAAGGAUCGGCACCCCAGUGGGUGGCUAUCCGUGGCAUUACAACUAGUGACAAUCAUGCGUGUUCCAUUUUCCUUGGAACAUGGUCUCGAGAGUGUAAAAUCCAUAGUACCCAUCAGUGUAGUCCAGCCUUCCGCACGAAUUAUACAUGGAACUCACAAAAACUCCGUAUAUAAACGUCACGUGCCAGUGAUAUUUAUGGAAUACCUAUUGCUGUAG'))