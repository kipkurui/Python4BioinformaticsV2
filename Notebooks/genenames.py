#!/usr/bin/env bash

import sys

input_text_file = sys.argv[1]
output_text_file = sys.argv[2]

def gene_names():
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
gene_names()

