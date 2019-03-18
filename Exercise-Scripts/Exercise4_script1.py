#!/bin/bash
d = { 'A': 'T', 'T' : 'A', 'G' : 'C' , 'C': 'G'}
#print (d)

sequence= input ("enter your sequence: ") # Exercise4-script1 modified.
mySeq = list (str(sequence)) 
#print (mySeq)
mySeq.reverse()
#print (mySeq)
complement = [d[base] for base in mySeq]
R_complement = "".join(complement)
print (R_complement)