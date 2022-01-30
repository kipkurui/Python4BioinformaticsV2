#EXERCISE 01,NOTEBOOK 02.

##FUNCTION 01.
trna='AAGGGCTTAGCTTAATTAAAGTGGCTGATTTGCGTTCAGTTGATGCAGAGTGGGGTTTTGCAGTCCTTA'
#BA='AAAAATCCCGAGGCGGCTATATAGGGCTCCGGAGGCGTAATATAAAA'
def percent_Base_content(dna):
    length=len(dna)
    A_count=dna.count('A')
    C_count=dna.count('C')
    G_count=dna.count('G') 
    T_count=dna.count('T')
    GC_content = G_count + C_count
    AT_content = A_count + T_count
    GC_percent = (GC_content/length)*100 
    AT_percent = (AT_content/length)*100
    #return print('AT and GC percent values:%s%s %s%s'% (AT_percent,'%',GC_percent,'%'))
    #return print('AT and GC percent values:%.3f%s %.3f%s'% (AT_percent,'%',GC_percent,'%'))
    return print(' AT percent value:%.3f%s%s'% (AT_percent,'%','\n'),'GC percent value:%.3f%s'% (GC_percent,'%'))
percent_Base_content(trna)

##FUNCTION 02.
##part one; to find the first, last and fifth amino acid of the given protein sequence.
aa='MNKMDLVADVAEKTDLSKAKATEVIDAVFA'
def aa_postions(*args):
    first_pos=aa[0]
    last_pos=aa[-1]
    fifth_pos=aa[4]
    return print(' aa_first_position: %s%s'%(first_pos,'\n'),'aa_last_position: %s%s'%(last_pos,'\n'),'aa_fifth_position: %s'%(fifth_pos))

aa_positions(aa)

##part two; on identifying the restriction site on the dna sequence.
BA='AAAAATCCCGAGGCGGCTATATAGGGCTCCGGAGGCGTAATATAAAA'
RE='TCCGGA'
#RX='TCC'
def first_restriction_site(X):
    BA_length=len(BA)
    RE_length=len(X)
    RE_position1=BA.find(X)
    RE_position2=BA.find(X)+RE_length
    #first_RE_postion = (RE_position1,RE_position2)
    #print(BA_length, RE_length, first_RE_postion)
    return print(' RE_start_position:%s%s%s' %(RE_position1,'th base','\n'), 'RE_stop_position:%s%s' %(RE_position2,'th base'))

first_restriction_site(BA)


#EXERCISE ONE, NOTEBOOK 04

##FUNCTION 01
seq1='AAAAATCCCGAGGCGGCTATATAGGGCTCCGGAGGCGTAATATAAAAG'
#seq1_1='GTGCCAATCCCGAGGCGGCTATATAGGGCTCCGGAGGCGTAATATAAAAGGA', for funtion checking.

def reverse_comp1(dseq):
    seq1_list=[dseq]
    reversed_seq1=dseq[::-1]
    seq2=reversed_seq1.replace('A','t').replace('T','a').replace('G','c').replace('C','g')
    Cseq2=seq2.upper()
    return print(Cseq2)

reverse_comp1(seq1)

##FUNCTION 02
seq1='AAAAATCCCGAGGCGGCTATATAGGGCTCCGGAGGCGTAATATAAAAG'
# seq1_1='GTGCCAATCCCGAGGCGGCTATATAGGGCTCCGGAGGCGTAATATAAAAGGA'
# Bw='ATATGGCT'
comp_seq1=[]
def reverse_comp2(dseq2):  
    for X in dseq2:
        if X ==('G'):
            comp_seq1.append('C')
        elif X ==('T'):
            comp_seq1.append('A')
        elif X ==('A'):
            comp_seq1.append('T')
        elif X ==('C'):
            comp_seq1.append('G')
        else:
            comp_seq1.append(X)
    comp_seq1.reverse()
    y=''.join(comp_seq1)
    return print(y)
    
reverse_comp2(seq1)

##FUNCTION 03
seq1='AAAAATCCCGAGGCGGCTATATAGGGCTCCGGAGGCGTAATATAAAAG'
#seq1_1='GTGCCAATCCCGAGGCGGCTATATAGGGCTCCGGAGGCGTAATATAAAAGGA'
#Bw='ATATGGCT'
def reverse_comp3(dseq3):
    rev_dna_dict = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}
    comp_seq2 = ''
    for base in dseq3:
        comp_seq2 = rev_dna_dict[base] + comp_seq2
    return print(comp_seq2)
    
reverse_comp3(seq1)




#EXERCISE 01, NOTEBOOK 05

##FUNCTION 01
x=0
def variables(x):
    while x<=5:
        print(x)
        x+=1
        
variables(0)

##FUNCTION 02
x=0
def variables1(x):
    while x<=10:
        if x==5:
            x+=1
            continue
        print(x)
        x+=1
        
variables1(0)

##FUNCTION 03
def variables2(a,b):
    for factor in range(a,b):
        print(factor)
        
variables2(4,11)




#EXERCISE 01, NOTEBOOK 06

mydna = "CAGTGATGATGACGAT"
yourdna = "ACGATCGAGACGTAGTA"
testdna = "ATFRACGATTGHAHYAK"
incdna="ATGGTGA"

##FUNCTION 01
#to calucalate the GC content and the %GC output from the given data.
def percentageGC1(seq):
    '''
    Takes a DNA string and returns %GC content
    
    '''
    seq=seq.upper() # helps to print any 
    GC_content=((seq.count('G')+seq.count('C'))/len(seq))*100
    print('The GC_content: %.2f%s ' % (GC_content,'%'))

percentageGC1(mydna)

##FUNCTION 02 
#design a function to test for the validity of the dna seq given.
def truedna(seq1):
    nucleotides=set('ATGC')
    xd=set(seq1)
    if xd==nucleotides:
        return True
    else:
        return False

truedna(mydna)

##FUNCTION 01/02 COMBINED 
#to calucalate the GC content in % output from the given data provided its a valid dna.
def percentageGC(seq):
    truedna(seq)
    if truedna(seq) == True: 
        GC_content=((seq.count('G')+seq.count('C'))/len(seq))*100
        print('%.2f %s ' % (GC_content,'%'))
    else:
        print('This is an invalid dna')

percentageGC(incdna)



#EXERCISE 01,02,03 NOTEBOOK 07

def gene_namez():
    with open('../Data/humchrx.txt', 'r') as myfile:
        with open('../Data/gene_names.txt', 'w') as myfile01:
            fetche_file = myfile.readlines()
            xz=fetche_file[33:]
            for x in xz:
                fileX=x.split(" ")[0]
                if fileX.startswith('-'):
                    break
                #print(f)
                myfile01.write(f'{fileX}\n')

gene_namez()



import sys
fileX_input=sys.argv[1]
fileX_output=sys.argv[2]

def gene_namez():
    with open(fileX_input) as myfile:
        with open(fileX_output) as myfile01:
            fetche_file = myfile.readlines()
            xz=fetche_file[33:]
            for x in xz:
                fileX=x.split(" ")[0]
                if fileX.startswith('-'):
                    break
                #print(f)
                myfile01.write(f'{fileX}\n')

gene_namez()






