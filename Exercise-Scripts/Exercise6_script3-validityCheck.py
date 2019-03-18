#!/bin/bash
def validSequence(sequence):
        valid = 'ACTG'
        for base in sequence:
            if base   not in valid:
                return("is not a valid DNA sequence")
            
DNA_test = validSequence(input("paste here your sequence: "))
print ("my sequence  %s" % (DNA_test))
