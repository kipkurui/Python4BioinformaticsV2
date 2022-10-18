# Assignment on conversion of scripts to functions

## Exercise_notebook_02
#Calculate the % GC and % AT content in the trna sequence
trna='AAGGGCTTAGCTTAATTAAAGTGGCTGATTTGCGTTCAGTTGATGCAGAGTGGGGTTTTGCAGTCCTTA'
def percent_gc(dna,*args):
    percent=((dna.count('G')+dna.count('C'))/len(dna) *100)
    percent1=((dna.count('A')+dna.count('T'))/len(dna) *100)
    return print(' The percentage is %.2f%s%s' % (percent,'%','\n'),'The percentage is %.2f%s'%(percent1,'%'))
percent_gc(trna)

## Amino acid positions
amino_acid='MNKMDLVADVAEKTDLSKAKATEVIDAVFA'
def amino_seq(x):
    print(x[0],x[4],x[-1],sep='\n')
amino_seq(amino_acid)


##The above amino acid is a bacterial restriction enzyme that recognizes "TCCGGA". Find the first restriction site in the following sequence: AAAAATCCCGAGGCGGCTATATAGGGCTCCGGAGGCGTAATATAAAA
dna_seq='AAAAATCCCGAGGCGGCTATATAGGGCTCCGGAGGCGTAATATAAAA'
def restriction_site(x):
    restrict_enzy='TCCGGA'
    rest_pos=x.find(restrict_enzy)
    end=rest_pos+len(restrict_enzy)
    return(rest_pos,end)
restriction_site(dna_seq)

## Exercise_Notebook_4
# using lists
dna='AAAAATCCCGAGGCGGCTATATAGGGCTCCGGAGGCGTAATATAAAA'
def lis_fun():
    reverse_dna=dna.replace('T','a').replace('A','t').replace('G','c').replace('C','g')
    reverse_dna=reverse_dna[::-1]
    reverse_dna=reverse_dna.upper()
    return(reverse_dna)
lis_fun()

# Using conditionals
comp_dna=[]
def reverse_comp(dna_seq):
    for base in dna_seq:
        if base == ('T'):
            comp_dna.append('A')
        elif base == ('A'):
            comp_dna.append('T')
        elif base == ('G'):
            comp_dna.append('C')
        elif base == ('C'):
            comp_dna.append('G')
        else:
            comp_dna.append(base)
    comp_dna.reverse()  
    y=''.join(comp_dna)
    return(y)
reverse_comp(dna)

# Using dictionaries
# using dictionaries
dna = 'AAAAATCCCGAGGCGGCTATATAGGGCTCCGGAGGCGTAATATAAAAG'
def dict_func(seq):
    dna_dict = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}
    rev_dna = ''
    for seq in seq:
        rev_dna = dna_dict[seq] + rev_dna
    return(rev_dna)
dict_func(dna)

## Notebook_5
1.Create a while loop that starts with x = 0 and increments x until x is equal to 5. Each iteration should print to the console.
x=0
def conditionals(x):
    while x<=5:
        print(x)
        x+=1
conditionals(0)

2. Repeat the previous problem, but the loop will skip printing x = 5 to the console but will print values of x from 6 to 10.

x=0
def skipping(x):
    while x<=10:
        if x==5:
            x+=1
            continue
        print(x)
        x+=1
skipping(0)

3. Create a for loop that prints values from 4 to 10 to the console.

def range_value(x,y):
    for i in range(x,y):
        print(i)
range_value(4,11)


## Notebook_6

### Exercise Let's return to our earlier exercise: calculating %GC content. In this exercise:

### Write a function percentageGC that calculates the GC content of a DNA sequence
### The function should return the %GC content
### The Function should return a message if the provided sequence is not DNA (This should be checked by a different function, called by your function)

## DNA checker function
seq='CAGTGATGATGACGAT'
def dna_checker(seq):
    for nuc in seq:
        if nuc not in 'ATCG':
            return False
    return True
dna_checker(seq)

## A function that calculates percentage GC and AT
mydna = "CAGTGATGATGACGAT"
yourdna = "ACGATCGAGACGTAGTA"
testdna = "ATFRACGATTGHAHYAK"
def percent_gc(seq):
    if dna_checker(seq):
        total_gc=(seq.count('G')+seq.count('C'))/len(seq)*100
        print(f'The percentage GC is {total_gc:.2f}')
    else:
        print('This is not a valid DNA sequence')
percent_gc(yourdna)
 
## Notebook_7
##Write a function the reads the file (humchr.txt) and writes to another file (gene_names.txt) a clean list of gene names.

#The script is provided in another script named genenames.py
genelist=[]
def gene_names():
    with open('Data/humchrx.txt', 'r') as myfile:
        with open('Data/genenames.txt', 'w') as myfile2:
            file=myfile.readlines()
            #print(file)
            for x,line in enumerate(file):
                #print(x,line)
                if x > 35:
                    split_lines=line.split()
                    column=split_lines[0]
                    if column.startswith('-'):
                        break
                    myfile2.write(f'{column}\n' )
gene_names()


## Notebook_7
###Show that the DNA string contains only four letters.

import sys
import re

## Part 1

#Takes a DNA string
###Show that the DNA string contains only four letters.

def dna_prove(input_file):
    with open(input_file) as my_file:
        my_file = my_file.read()
        my_file2 = set(my_file.replace('\n',''))
        return(set(my_file2))
print(dna_prove(sys.argv[1]))


## Modified to take a fasta file

def dna_prove(input_file):
    sequence = ''
    with open(input_file) as my_file:
        for line in my_file:
            if line.startswith('>'):
                continue
            sequence += line
                
        sequence = (sequence.replace('\n',''))
        return(set(sequence))
print(dna_prove(sys.argv[1]))


 ## Part 2   
###In the DNA string there are regions that have a repeating letter. What is the letter and length of the longest repeating region?
    
def dna_prove(input_file):
    sequence = ''
    sequence_list = []
    with open(input_file) as my_file:
        for line in my_file:
            if line.startswith('>'):
                continue
            sequence += line
            sequence = (sequence.replace('\n',''))
            
        sequence_list.append(max(re.findall(r"A{2,}", sequence)))
        sequence_list.append(max(re.findall(r"G{2,}", sequence)))
        sequence_list.append(max(re.findall(r"T{2,}", sequence)))
        sequence_list.append(max(re.findall(r"C{2,}", sequence)))
        print(max(sequence_list))
        print(len(max(sequence_list)))
        
dna_prove(sys.argv[1])

## Part 3
### How many ’ATG’s are in the DNA string?

def dna_prove(input_file,string):
    sequence = ''
    sequence_list = []
    with open(input_file) as my_file:
        for line in my_file:
            # Remove the header line of a fasta file
            if line.startswith('>'):
                continue
            sequence += line
            # Removes new line character '\n'
            sequence = (sequence.replace('\n',''))
            # Gets the longest repeating pattern
        sequence_list.append(max(re.findall(r"A{2,}", sequence)))
        sequence_list.append(max(re.findall(r"G{2,}", sequence)))
        sequence_list.append(max(re.findall(r"T{2,}", sequence)))
        sequence_list.append(max(re.findall(r"C{2,}", sequence)))
        print(max(sequence_list))
        print(len(max(sequence_list)))

    print(sequence.count(string))
    
        #return(set(sequence))
#print(dna_prove(sys.argv[1]))
dna_prove(sys.argv[1],sys.argv[2])

