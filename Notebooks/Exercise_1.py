#!/home/user/miniconda3/bin/python

##Exercise 1_ Calculating GC and AT content

trna='AAGGGCTTAGCTTAATTAAAGTGGCTGATTTGCGTTCAGTTGATGCAGAGTGGGGTTTTGCAGTCCTTA'
len(trna)

A_total=trna.count('A')
C_total=trna.count('C')
G_total=trna.count('G')
T_total=trna.count('T')

GC_total=(trna.count("C") + (trna.count("G")))
AT_total=(trna.count("A") + (trna.count("T")))

GC_content=(GC_total/len(trna))*100
AT_content=(AT_total/len(trna))*100
print("The percent GC content of the sequence is %d"%GC_content)
print("The percent AT content of the sequence is %d"%AT_content)
