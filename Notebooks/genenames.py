#!/usr/bin/env bash

import sys

def gene_names(input_text_file, output_text_file):
    """
    Takes two arguments from the commandline
    input file contain the genes and an output
    file to which gene name will be written to.
    """
    
    with open(input_text_file) as in_file:
        with open(output_text_file, 'w') as out_file:
            file = in_file.readlines()
            for x,line in enumerate(file):
                if x > 35:
                    split_lines = line.split()
                    field = split_lines[0]
                    if field.startswith('-'):
                        break
                    out_file.write('{}\n'.format(field))
# Calling the function
gene_names(sys.argv[1], sys.argv[2])

