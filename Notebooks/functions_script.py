#!/usr/bin/env python

#Notebook_2 Excerses
#Calculate the % GC and % AT content in the trna sequence
dna = 'AAGGGCTTAGCTTAATTAAAGTGGCTGATTTGCGTTCAGTTGATGCAGAGTGGGGTTTTGCAGTCCTTA'
def GCPercentage(dna):
    """
    Takes DNA sequence and return the percentage of 
    GC content
    """
    C_count=dna.count('C')
    G_count=dna.count('G')

    length_dna = len(dna)

    # GC Content %
    total_gc_content = G_count + C_count
    gcpercent = (total_gc_content / length_dna) * 100
    return('{:.2f}%'.format(gcpercent))
    
def ATPercentage(dna):
    """
    Takes DNA sequence and return the percentage of 
    AT content
    """
    A_count=dna.count('A')
    T_count=dna.count('T')

    length_dna = len(dna)
   
    # AT Content %
    total_AT_content = T_count + A_count 
    percentage_AT = (total_AT_content / length_dna) * 100
    return('{:.2f}%'.format(percentage_AT))


#Given the following amino acid sequence (MNKMDLVADVAEKTDLSKAKATEVIDAVFA), 
#find the first, last and the 5th amino acids in the sequence.
amino = 'MNKMDLVADVAEKTDLSKAKATEVIDAVFA'

def findAmino(amino):
    for i,a in enumerate(amino):
        if i == 0: # The first aa
            print(a)
        elif i == 4: # The Fifth aa
            print(a)
        elif i == (len(amino) - 1): # The last aa
            print(a)
            
#The above amino acid is a bacterial restriction enzyme that
#recognizes "TCCGGA". Find the first restriction site in 
#the following sequence: AAAAATCCCGAGGCGGCTATATAGGGCTCCGGAGGCGTAATATAAAA
dna_seq = 'AAAAATCCCGAGGCGGCTATATAGGGCTCCGGAGGCGTAATATAAAA'
site = "TCCGGA"
def restrictionSite(dna_seq, site):
    return(dna_seq.find(site))


# Notebook_4
#Exercise
#Using strings, lists, tuples and dictionaries concepts, find the 
#reverse complement of AAAAATCCCGAGGCGGCTATATAGGGCTCCGGAGGCGTAATATAAAA
#Algorithm:
# Question1
dna = 'AAAAATCCCGAGGCGGCTATATAGGGCTCCGGAGGCGTAATATAAAA'
def reverseDnaStr(dna):
    reversed_dna = dna.replace('A','t').replace('C','g').replace('G','c').replace('G','c').replace('T','a')
    reversed_dna = dna[::-1]
    reversed_dna = reversed_dna.upper()
    return(reversed_dna)

# list function
def reverseDnaLst(dna_seq):
    dna_comp = []
    for base in dna_seq:
        if base == ('T'):
            dna_comp.append('A')
        elif base == ('A'):
            dna_comp.append('T')
        elif base == ('G'):
            dna_comp.append('C')
        elif base == ('C'):
            dna_comp.append('G')
        else:
            dna_comp.append(base)
    dna_comp.reverse()
    d = ''.join(dna_comp)
    return(d)


# using dictionaries
dna = 'AAAAATCCCGAGGCGGCTATATAGGGCTCCGGAGGCGTAATATAAAAG'
def reverseDnaDict(seq):
    dna_dict = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}
    rev_dna = ''
    for seq in seq:
        rev_dna = dna_dict[seq] + rev_dna
    return(rev_dna)
reverseDnaDict(dna)


# Notebook 5
#Create a while loop that starts with x = 0 and increments 
#x until x is equal to 5. Each iteration should print to the console.
x=0
def increment(x):
    while x<=5:
        print(x)
        x+=1
        

#Repeat the previous problem, but the loop will skip printing 
#x = 5 to the console but will print values of x from 6 to 10.
x=0
def skipPrint(x):
    while x<=10:
        if x==5:
            x+=1
            continue
        print(x)
        x+=1
        
#Create a for loop that prints values from 4 to 10 to the console.
def valuePrint(a,b):
    for x in range(a,b):
        print(x)
valuePrint(4,11)


# Write a function percentageGC that calculates the GC content of a DNA sequence
def dnaSeqeunceValidator(dna):
    """A fucntion that validates a DNA sequence
    """
    clean_dna_sequence = ''
    if dna:
        for base in dna:
            if base.upper() not in ('A','T','C','G', 'N'):
                print("Invalid character '{}' at index position '{}'".format(base, dna.index(base)))
                return(False, 0)
            else:
                clean_dna_sequence += base.upper()
    else:
        print('Please provide a valid sequence')
    return(True, clean_dna_sequence)         
    
    
def percentageGC(sequence):
    """
    Takes a sequence of DNA and calculates the percentage of GC content
    """
    # Validates the DNA sequence provided
    flag, dna_seq = dnaSeqeunceValidator(sequence)
    if flag and dna_seq:
        GC_percentage = (dna_seq.upper().count('G') + dna_seq.upper().count('C'))/len(dna_seq) * 100
        return('GC = {:.2f}%'.format(GC_percentage))
    else:
        print('The sequence has an Invalid character(s) which is not part of a DNA sequence')
        
percentageGC('ttgtft')


def gene_names():
    with open('../Data/humchrx.txt') as in_file:
        with open('../Data/genenames.txt', 'w') as out_file:
            file = in_file.readlines()
            for x,line in enumerate(file):
                if x > 35:
                    split_lines = line.split()
                    field = split_lines[0]
                    if field.startswith('-'):
                        break
                    out_file.write('{}\n'.format(field))
gene_names()
