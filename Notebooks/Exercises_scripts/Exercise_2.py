#!/home/user/miniconda3/bin/python

## Finding the first, last and the fifth amino acids in 'MNKMDLVADVAEKTDLSKAKATEVIDAVFA'

aa_seq="MNKMDLVADVAEKTDLSKAKATEVIDAVFA"
print("The first amino acid in sequence is", aa_seq[0])
print("The last amino acid in sequence is", aa_seq[-1])
print("The fifth amino acid in the sequence is", aa_seq[5-1])


##  Finding the first restriction site in the sequence: "AAAAATCCCGAGGCGGCTATATAGGGCTCCGGAGGCGTAATATAAAA"

seq="AAAAATCCCGAGGCGGCTATATAGGGCTCCGGAGGCGTAATATAAAA"
len(seq)

Restricion_site="TCCGGA"
print(Restricion_site)
print(seq.find(Restricion_site))