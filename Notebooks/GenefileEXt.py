import sys
def get_genes_names(infile, outfile): #exercise2 final script.
    #input_file = humchrx.txt
    with open (infile,'r') as humchrx:
        tag = False
        for line in humchrx:
            if line.startswith('name'):
                #print(line)
                tag = True
            if line.startswith('-'):
                tag= False
            #if line.startswith('-'):
             #continue
            if tag == True:
                lineList = line.split()
                if len(lineList) > 0:
                    #print(lineList[0])
                    data = (lineList[0])
                    #print(data)
                    with open(outfile,'a') as newfile:
                        print(data, file=newfile)
infile = sys.argv[1]
outfile = sys.argv[2]
get_genes_names('../Data/humchrx.txt', '../Data/gene_names.txt') 