#Calculate the % GC and % AT content in the trna sequence
trna='AAGGGCTTAGCTTAATTAAAGTGGCTGATTTGCGTTCAGTTGATGCAGAGTGGGGTTTTGCAGTCCTTA'
def percent_gc(dna,*args):
    percent=((dna.count('G')+dna.count('C'))/len(dna) *100)
    percent1=((dna.count('A')+dna.count('T'))/len(dna) *100)
    return print(' The percentage is %.2f%s%s' % (percent,'%','\n'),'The percentage is %.2f%s'%(percent1,'%'))
percent_gc(trna)


