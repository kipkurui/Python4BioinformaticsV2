#!/bin/bash
sequence= 'AAAAATCCCGAGGCGGCTATATAGGGCTCCGGAGGCGTAATATAAAA' # Exercise 2 script3
print ("The restriction site starts at position %d and ends at %d"  %(sequence.index("TCCGGA"),\
                                                                      int(sequence.index("TCCGGA")+5) ))