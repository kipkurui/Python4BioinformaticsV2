"""
Name: Get_Gene_List

Author: Caleb Kibet

Version: 0.01

Date: Dec 2020

Usage:
    python get_gene_list.py <annotation file> <gene list out>
    
    eg: python get_gene_list.py ../Data/humchrx.txt test_command.txt
"""

import sys
def write2file(gene_list, out_file):
    """
    Takes a gene list and writes the output to file
    """
    with open(out_file, 'w') as outfile:
        outfile.write('\n'.join(gene_list))

def remove_empty(gene_list):
    """
    Given a gene list, removes items 
    that start with dash (empty)
    """
    tag = True
    while tag:
        try:
            gene_list.remove('-')
        except ValueError:
            tag = False
    return gene_list

def clean_genes(input_file, out_file):
    """
    Given a chromosome annotation file, extract the 
    genes and write them to another file
    """
    gene_list = []
    tag = False
    with open(input_file, 'r') as humchrx:
        for line in humchrx:
            if line.startswith('Gene'):
                tag=True
            if line == '\n':
                tag = False
            if tag:
                gene_list.append(line.split()[0])
    #clean the gene list
    gene_list.pop(2)
    gene_list[0] = gene_list[0]+"_"+gene_list[1]
    gene_list.pop(1)
    
    gene_list = remove_empty(gene_list)
    
    ## Writing to file
    write2file(gene_list, out_file)
if len(sys.argv) < 3:
    print(__doc__)
else:
    clean_genes(sys.argv[1], sys.argv[2])