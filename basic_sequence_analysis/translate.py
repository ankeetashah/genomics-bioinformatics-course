#translates sequence in wcfr.fasta. Makes the assumption that this is the template strand, and all Ts can be treated as Us. 

#Start by pasting in the sequence
sequence = "ATGAAAATACCTTTTTCACCACCTTATATTGACGAGGCGGTCATCAACGAAGTCGTTGATTCGTTACGTTCCGGTTGGATCACATCCGGTCCGAAAGTGAAGGCTTTGGAGGAAGAAATTAAATCTTTCTCAGGAGCAAAAGAAGTGCTTTGTGTCAATTCCTGGACATCAGGAGCTATTATGATGTTGCGTTGGCTGGGAGTGAAGGAGGGCGATGAAGTGATTGTTCCTGCCTATACTTACAGTGCAACGGCATTGGCTGTGCTCCATGCCGGAGCCAAACCGGTAATGGTGGATTCCGGAACTGATTTTAATATTTCGGTGGAGGCTGTTCGTAAAGCTATTACTCCTAAAACAAAGGCGATTATACCCGTAGATATTGCTGGTTTTCCCTGCGATTATGAAAGAATCATGGCACTGGTGCAGGAACCAGAAATGGTAAAACTGTTCCGTTCGGAATCTCCTGTGCAAGAAAAATTGGGACGCATCTTGGTGATGAATGATGCTGCCCACTCTTTGGGAGCACGTTACAGTAGCCGTCAGCGTACCGGTTGTGAAACTGATGTGGCTATCTTTTCACTTCATGCCGTGAAAAATGTGACTACTGCCGAAGGTGGGGCCATTTGCCTGAATCTGCCTAAGCCGTTCGATAATACGGAGTTGTATAAAGAGCTACGGATGACAAGCTTGAACTGCCAGACCAAGGATGCTTTTTCGAAATCTAAAGCCGGAGGATGGCGTTATGATATTGTCGGTTTCGGGATGAAAATCAATATGGCCGATGTAAATGCCGCCATAGGACTGGCACAGATACGAGAATATCCGGAATTGCTGAAAGAACGAAAGCGGGTGTTTAATGCTTATAGCGATGCTTTTTCGGCTTGTGACTGGGCCATCGTTCCGCCTTCTGTGGATGGGGAAAAGGAAAGCTCTTATCACATTTATGCTTTGCGTATTAAGGACTTTACCGAAGAACAACGCGACCGGATGATTGATGAAATCGCTAAAAGTGAAGTGGCTGTCAATGTGCACTTTATACCGATGCCGATGTTGTCGTTCTTCAAATCGATGGGATATGATATAAAGGATTATCCACAGGCTTATCAGAACTTTAAGAGCGAGATATCATTGCCGATATATCCCCAATTGGATAGTGAAAAATTGAATTTCATTATTGAAACCGTAAAGGCGGCCTATGCGACCGTAATTGCAGAAAACCGATAG"

#create a list of codons 
list_sequence = [sequence[x:x+3] for x in range(0,len(sequence),3)]


#create an empty protein
protein = ""

#a long "dictionary" of codons (keys) and amino acids (values)
translate = {
        'TTT' : 'F', 
        'TTC' : 'F', 
        'TTA' : 'L', 
        'TTG' : 'L', 
        'CTT' : 'L', 
        'CTC' : 'L', 
        'CTA' : 'L', 
        'CTG' : 'L', 
        'ATT' : 'I', 
        'ATC' : 'I', 
        'ATA' : 'I', 
        'ATG' : 'M', 
        'GTT' : 'V', 
        'GTC' : 'V', 
        'GTA' : 'V', 
        'GTG' : 'V',
        'TCT' : 'S',
        'TCC' : 'S',
        'TCA' : 'S',
        'TCG' : 'S',
        'CCT' : 'P',
        'CCC' : 'P',
        'CCA' : 'P',
        'CCG' : 'P',
        'ACT' : 'T',
        'ACC' : 'T',
        'ACA' : 'T',
        'ACG' : 'T',
        'GCT' : 'A',
        'GCC' : 'A',
        'GCA' : 'A',
        'GCG' : 'A',
        'TAT' : 'Y',
        'TAC' : 'T',
        'TAA' : 'X',
        'TAG' : 'X',
        'CAT' : 'H',
        'CAC' : 'H',
        'CAA' : 'Q',
        'CAG' : 'Q',
        'AAT' : 'A',
        'AAC' : 'A',
        'AAA' : 'K',
        'AAG' : 'K',
        'GAT' : 'D',
        'GAC' : 'D',
        'GAA' : 'E',
        'GAG' : 'E',
        'TGT' : 'C',
        'TGC' : 'C',
        'TGA' : 'X',
        'TGG' : 'X',
        'CGT' : 'R',
        'CGC' : 'R',
        'CGA' : 'R',
        'CGG' : 'R',
        'AGT' : 'S',
        'AGC' : 'S',
        'AGA' : 'R',
        'AGG' : 'R',
        'GGT' : 'G',
        'GGC' : 'G',
        'GGA' : 'G',
        'GGG' : 'G'
}

#use a loop to go through each of the codons in list_sequence and find the corresponding amino acid. 
for c in list_sequence:
    protein = protein + translate.get(c)

#avoid if-else by splitting the string before the first X
print protein.split("X",1)[0] 

