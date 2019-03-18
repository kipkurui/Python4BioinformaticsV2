#!/bin/bash
def percentageGC(dnaseq):
    for base in dnaseq:
        G_count = dnaseq.count ('G')
        C_count = dnaseq.count ('C')
        GC_Sum = G_count + C_count
        return (GC_Sum / len(dnaseq))*100 
GC_percent =percentageGC(input ("paste here your DNA sequence: "))
        
print("The percent GC content is %.2f" %(GC_percent)) 
    
   