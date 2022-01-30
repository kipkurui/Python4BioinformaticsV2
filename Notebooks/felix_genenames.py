#! /usr/bin/env bash
import sys
fileX_input=sys.argv[1]
fileX_output=sys.argv[2]

def gene_namez():
    with open(fileX_input) as myfile:
        with open(fileX_output,'w') as myfile01:
            fetche_file = myfile.readlines()
            xz=fetche_file[33:]
            for x in xz:
                fileX=x.split(" ")[0]
                if fileX.startswith('-'):
                    break
                #print(f)
                myfile01.write(f'{fileX}\n')

gene_namez()


