#!/bin/bash
sequence = input("paste here your sequence:  ")
print("The length of the sequence is %i" % len(sequence),"nucleotides")
A_count=sequence.count('A')
C_count=sequence.count('C')
G_count=sequence.count('G')
T_count=sequence.count('T')
GC_percent=(G_count + C_count )/ len(sequence) * 100
AT_percent=(A_count + T_count )/ len(sequence) * 100
print ("The sequence has Gc content of %.2f and AT content of %.2f. The length of the DNA is %i "\
% (GC_percent, AT_percent, len(sequence)))
