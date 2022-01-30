#!usr/bin/env bash
import sys
gene_file_input = sys.argv[1]
gene_file_output = sys.argv[2]

def gene_names():
    with open(gene_file_input) as myfile:
        with open(gene_file_output) as myfile2:
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