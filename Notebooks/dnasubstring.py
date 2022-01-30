#!/usr/bin/env python

import sys

input_text_file = sys.argv[1]
substring = sys.argv[2]

def gene_names(input_text_file, substring):
    with open(input_text_file) as in_file:
        dnastr = in_file.read()
        dnasub = dnastr.count(substring)
        print(dnasub)