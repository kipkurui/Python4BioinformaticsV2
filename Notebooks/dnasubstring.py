#!/usr/bin/env python

import sys
import re

# def showDnaSeq(dna_file):
#     with open(dna_file) as fh:
#         dnastr = fh.read()
#         dnastr = dnastr.replace('\n', '')
#         return(set(dnastr))

# print('The DNA contains: ', showDnaSeq(sys.argv[1]))

# Adapts to a .fa with the header line
def showDnaSeq(dna_file):
    dnastr = ''
    with open(dna_file) as fh:
        for line in fh:
            if line.startswith('>'): continue
            dnastr += line
        dnastr = dnastr.replace('\n', '')
        return(set(dnastr))

#print('The DNA contains: ', showDnaSeq(sys.argv[1]))

def showDnaSeq(dna_file, substring):
    dnastr = ''
    longest_dna = []
    
    with open(dna_file) as fh:
        for line in fh:
            # Removes the first line in .fa file
            if line.startswith('>'): continue
            dnastr += line
         # Removes the \n from the string and concatenate
        dnastr = dnastr.replace('\n', '')
        #dnalst = list(set(dnastr))
           # Gets the longest sequnce of A/T/G/C and appends
            # it to a list.
        longest_dna.append(max(re.findall(r'A{2,}', dnastr)))
        longest_dna.append(max(re.findall(r'G{2,}', dnastr)))
        longest_dna.append(max(re.findall(r'T{2,}', dnastr)))
        longest_dna.append(max(re.findall(r'C{2,}', dnastr)))
        
        print(max(longest_dna))
        print(len(max(longest_dna)))
        print(dnastr.count(substring))
        
showDnaSeq(sys.argv[1], sys.argv[2])       
            
        #return(set(dnastr))

#print('The DNA contains: ', showDnaSeq(sys.argv[1]))
#showDnaSeq(sys.argv[1])