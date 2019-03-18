#!/home/user/miniconda3/bin/python

## Calculating the % GC content in 'AAGGGCTTAGCTTAATTAAAGTGGCTGATTTGCGTTCAGTTGATGCAGAGTGGGGTTTTGCAGTCCTTA' using functions.

seq="AAGGGCTTAGCTTAATTAAAGTGGCTGATTTGCGTTCAGTTGATGCAGAGTGGGGTTTTGCAGTCCTTA"
def percentGC(seq):
    seq_length=len(seq)
    G = seq.count('G')
    C = seq.count('C')
    percentGC = ((G+C)/seq_length)*100
    return(percentGC)



